# Stealth Script RPC Protocol

Binary RPC protocol for local interaction between Python scripts and 
the **[Stealth](https://uostealth.com/)** application (automation client for the MMORPG Ultima Online).

```
Python script ←— TCP/RPC —→ Stealth Client ←— UO Protocol —→ UO Game Server
```

---

## 1. Transport

Uses **TCP** protocol on the loopback interface (`127.0.0.1`). Byte order is **little-endian**.

Default provider port: **47602**. 
Actual data exchange occurs over a dedicated script port obtained during negotiation.

### Framing

Each packet is prefixed with a 4-byte length header:

```
┌───────────────────┬──────────────────────────────┐
│ Length (U32 LE)   │ Payload (Length bytes)       │
│ 4 bytes           │ variable length              │
└───────────────────┴──────────────────────────────┘
```

**Length** — size of the payload in bytes, excluding the field itself.

---

## 2. Connection Establishment

Two consecutive phases.

### Phase 1 — Port Negotiation

The client connects to the provider port and requests a dedicated port:

```
Client → Server:  _RequestPort(GroupId: U64, ProfileName: String)
Server → Client:  _FunctionResultCallback(CallId: U16, Result: tuple[U16, U64])
```

Response: **ScriptPort** (U16) + **ScriptGroup** (U64). After receiving this, the connection to the provider is closed.

### Phase 2 — Handshake

The client connects to the script port and sends the version:

```
Client → Server:  _LangVersion(Lang: U8, Major: U8, Minor: U8, Revision: U8, Build: U8)
```

No response is required. The connection is established.

---

## 3. Type System

### 3.1. Primitives

| Type   | Size    | Format | Description                   |
|--------|---------|--------|-------------------------------|
| `Bool` | 1 byte  | `<?`   | Boolean value                 |
| `U8`   | 1 byte  | `<B`   | Unsigned 8-bit                |
| `I8`   | 1 byte  | `<b`   | Signed 8-bit                  |
| `U16`  | 2 bytes | `<H`   | Unsigned 16-bit               |
| `I16`  | 2 bytes | `<h`   | Signed 16-bit                 |
| `U32`  | 4 bytes | `<I`   | Unsigned 32-bit               |
| `I32`  | 4 bytes | `<i`   | Signed 32-bit                 |
| `U64`  | 8 bytes | `<Q`   | Unsigned 64-bit               |
| `I64`  | 8 bytes | `<q`   | Signed 64-bit                 |
| `F32`  | 4 bytes | `<f`   | Floating point number         |
| `F64`  | 8 bytes | `<d`   | Floating point number         |

### 3.2. String

Encoding **UTF-16LE**.

```
┌──────────────────────┬─────────────────────────────┐
│ ByteLength (U32 LE)  │ UTF-16LE data               │
│ 4 bytes              │ ByteLength bytes            │
└──────────────────────┴─────────────────────────────┘
```

**ByteLength** — length in bytes, not characters.

### 3.3. DateTime

**F64** (8 bytes) — days since Delphi epoch `1899-12-30`.

### 3.4. Buffer

Raw bytes without a length prefix. Read until the end of the payload of the current packet. 
Used for `Result` in responses.

### 3.5. list[T]

Array of elements of the same type:

```
┌───────────────────┬──────────┬──────────┬─────┬──────────┐
│ Count (U32 LE)    │ Item[0]  │ Item[1]  │ ... │ Item[N-1]│
└───────────────────┴──────────┴──────────┴─────┴──────────┘
```

### 3.6. tuple[T1, T2, ...]

Sequence of values of different types **without** a length prefix. Elements are serialized consecutively in the order of declaration.

### 3.7. TypedTuple

Self-describing tuple — each value is prefixed with a type index byte. Used for event arguments.

```
┌──────────────┬───────────────┬─────────┬───────────────┬─────────┬─────┐
│ Count (U8)   │ TypeIdx (U8)  │ Value   │ TypeIdx (U8)  │ Value   │ ... │
└──────────────┴───────────────┴─────────┴───────────────┴─────────┴─────┘
```

| Index | Type     |
|-------|----------|
| 0     | String   |
| 1     | U32      |
| 2     | I32      |
| 3     | U16      |
| 4     | I16      |
| 5     | U8       |
| 6     | I8       |
| 7     | Bool     |

### 3.8. Structures

Composite types: fields are serialized sequentially in the order of declaration. 
Recursive — a field can be a primitive, list, string, or another structure.


### 3.9. Alignment

All data is written to the packet "tightly", without padding or alignment.

---

## 4. Packet Format

The payload inside the frame has a unified structure:

```
┌──────────────────┬──────────────────┬─────────────────────────┐
│ MethodID (U16)   │ CallID (U16)     │ Data (variable)         │
│ 2 bytes          │ 2 bytes          │ 0..N bytes              │
└──────────────────┴──────────────────┴─────────────────────────┘
```

- **MethodID** — identifier of the method
- **CallID** — call identifier for matching request/response
  - `0` — fire-and-forget (no response expected)
  - `1..65535` — cyclic increment: `id = id % 0xFFFF + 1`
- **Data** — serialized arguments (request) or result (response). The format is determined by the method specification.

---

## 5. Interaction Model

### 5.1. Request-Response (RPC)

```
Client                                     Server
  │                                          │
  │─── [MethodID, CallID, Args...] ────────→ │
  │                                          │  (execution)
  │←── [MethodID=1, CallID, Result] ──────── │
  │                                          │
```

1. The client assigns a `CallID` and registers a `Future`
2. Sends the packet `[MethodID, CallID, Args...]`
3. The server replies with `_FunctionResultCallback` (MethodID = 1) with the same `CallID`
4. The client matches the `CallID` and decodes the result

For fire-and-forget — `CallID = 0`, no response expected.

The client can send multiple requests at once, but the server will process/respond to them sequentially.

---

## 6. Service Packets (ID 1–12)

| ID | Name                         | Direction       | Arguments                             | Description / Reaction                  |
|----|------------------------------|-----------------|---------------------------------------|-----------------------------------------|
| 1  | `_FunctionResultCallback`    | Server → Client | `CallId: U16, Result: Buffer`         | Resolve `Future` by `CallId`            |
| 2  | `_StopScriptCallback`        | Server → Client | —                                     | Close connection                        |
| 3  | `_ErrorReportCallback`       | Server → Client | `Error: String`                       | Logging + close connection              |
| 4  | `_ScriptTogglePauseCallback` | Server → Client | —                                     | Toggle client pause                     |
| 5  | `_LangVersion`               | Client → Server | `Lang, Major, Minor, Rev, Build: U8`  | Handshake (client version)              |
| 6  | `_EventCallback`             | Server → Client | `EventId: U8, Args: TypedTuple`       | Dispatch event                          |
| 7  | `SetEventCallback`           | Client → Server | `EventIndex: U8`                      | Subscribe to event                      |
| 8  | `ClearEventCallback`         | Client → Server | `EventIndex: U8`                      | Unsubscribe from event                  |
| 9  | `_ScriptPathCallback`        | Server → Client | —                                     | Request path; response is `_ScriptPath` |
| 10 | `_ScriptPath`                | Client → Server | `ScriptName: String`                  | Response with script path               |
| 11 | `_SelectProfile`             | Client → Server | `ProfileName: String`                 | Select profile                          |
| 12 | `_RequestPort`               | Client → Server | `GroupId: U64, ProfileName: String`   | Request dedicated port                  |

---

## 7. Server Push Notifications

The server can initiate sending packets independently of client requests:

| Packet                       | Purpose                                   |
|------------------------------|-------------------------------------------|
| `_EventCallback`             | Asynchronous event notification           |
| `_StopScriptCallback`        | Request to terminate the script           |
| `_ScriptTogglePauseCallback` | Pause/resume script execution             |
| `_ErrorReportCallback`       | Error message                             |
| `_ScriptPathCallback`        | Request path to the script                |

### 7.1 Asynchronous Events

**Subscribe/Unsubscribe:**

```
Client → Server:  SetEventCallback(EventIndex: U8)
Client → Server:  ClearEventCallback(EventIndex: U8)
```

**Receive:**

```
Server → Client:  _EventCallback(EventId: U8, Args: TypedTuple)
```

Event arguments are encoded in the `TypedTuple` format (section 3.7), which allows the server to transmit arbitrary sets of parameters without a fixed schema.

## 8. Error Handling

If an unrecoverable error occurs during call processing, the server will notify the client and drop the connection.

```
Server → Client:  ErrorReportCallback(Error: String)
```
