Basic classes
=============

`ApiSpecification` is a base class used to declare APIs, `StealthApi` is its implementation, 
describing the UO Stealth Client API.

`AsyncRPCClient` - Client interface description. `AsyncStealthClient` is a concrete implementation 
of the UO Stealth Client RPC protocol.

`RPCType` - a base data type interface that provides methods for serialization and deserialization.
It implements serialization of lists (arrays) of identical elements and tuples (sequences of elements).

`PrimitiveType` - a primitive data type representing only one value, 
implements serialization methods using the `struct` module.

`StructType` is a composite data type consisting of multiple value fields. 
Fields are serialized recursively if necessary.


Stealth related-classes
=======================

The `stealth_types.py` file describes the basic types used in the API, 
such as integers/floats, strings, and datetimes.

The file `stealth_structs.py` describes composite (structure) types.

`StealthApi` is a declarative description of the UO Stealth client API. 
It only requires declaring a function, annotating its arguments and return type, 
and using the `@method_api(int)` decorator to associate the method 
with its numeric identifier. 

Arguments and return values must inherit from `RPCType`.
For arrays, the notation `list[U8]`, `list[WorldPoint]` is used.

For example:

```py
class StealthApi(ApiSpecification):
    @method_api(14)
    def GetSelfID(self) -> U32:
        pass

    @method_api(381)
    def GetMultiAllParts(self, MultiID: U32) -> list[MultiPart]:
        pass

    @method_api(438)
    def IsWorldCellPassable(self, CurrX: U16, CurrY: U16, CurrZ: I8, DestX: U16, DestY: U16, WorldNum: U8) -> tuple[Bool, I8]:
        pass
```

`StealthRPCEncoder` - A helper class responsible for encoding arguments into binary format and decoding binary results back into Python types. 
It handles the low-level details of packing and unpacking data according to the protocol.

`AsyncStealthRPCProtocol` initially splits the received bytes into individual packets 
and passes them to the `AsyncRPCClient`, in this case `AsyncStealthClient`

`StealthSession` - Manages script identity (group, profile, script name) and connection parameters.

Provides port negotiation via `negotiate_port()` method, which connects to the main Stealth port 
to request a dedicated script port. Thread-safe for concurrent use across multiple event loops.

Sessions are reusable - one session can be shared between multiple clients. This separates 
script identity from the API client, enabling multi-client scenarios. Supports legacy mode 
(reading script port from command-line arguments).

`AsyncStealthClient` manages the connection to the UO Stealth Client 
and the reception and transmission of information about called functions 
and their results over this connection. It accepts an optional `StealthSession` 
parameter to control its identity and connection parameters.

Method - `call_method` receives the method specification and its argument list, 
packs them into bytes, and sends them to the UO Stealth Client. 
It also waits for the method's execution result, if necessary, and decodes the result.

`AsyncStealthApiClient` is an endpoint - it is a client and provides us with access to the API.
It inherits the `AsyncInterface` class and `AsyncStealthClient`. 
`AsyncInterface` is simply a stub with methods for IDE hints.

Method binding is performed by the `implement_api` decorator, which receives an `ApiSpecification`
class as an argument, describing the API, and a `method_factory` that simply returns a closure method 
that handles this call.

While `AsyncStealthApiClient` provides the core asynchronous interface, the library also includes wrappers 
for synchronous usage, which can be more convenient for simple scripts or those migrating from `py_stealth`.

`SyncStealthApiClient` a synchronous adapter that wraps `AsyncStealthApiClient` and 
uses a `StealthContext` to execute async operations synchronously.

`AsyncStealthApiClient` and `SyncStealthApiClient` accept optional parameter **`session`** 
a `StealthSession` instance defining the script identity and connection parameters.
If not provided, a new unique `StealthSession` is automatically created.

`SyncStealthApiClient` also accepts optional parameter - **`context`** 
a `StealthContext` instance defining how coroutines are executed. 
If not provided, a new `StealthSession` instance will be created.


Execution Contexts
==================

`StealthContext` - Abstract base class defining WHERE and HOW coroutines are executed. 
Provides `run_coroutine(coro)` method to bridge synchronous code and asynchronous core.

**Implementations**:

`ThreadedContext` - Executes coroutines in a dedicated background thread with its own asyncio event loop.
Thread-safe, isolated from main thread.

`FastContext` - Executes coroutines in the current thread's event loop. Lower overhead, blocks until completion. 
Not thread-safe, cannot be used from within a running event loop. 

`DefaultContextManager` - Singleton managing a shared global `ThreadedContext`. 
Used automatically when no context is explicitly provided to `SyncStealthApiClient`.

Example usage:

```python
# Simple usage with defaults (global ThreadedContext + new session)
with SyncStealthApiClient() as client:
    client.AddToSystemJournal("Hello from Python!")

# Custom context (dedicated thread for this client)
from py_astealth.sync.context import ThreadedContext

context = ThreadedContext(name="my-client-thread")
client = SyncStealthApiClient(context=context)

# Fast context (runs in current thread, lower overhead)
from py_astealth.sync.context import FastContext

client = SyncStealthApiClient(context=FastContext())

# Shared session across multiple clients
from py_astealth.stealth_session import StealthSession
session = StealthSession(profile="(0)", script_name="multi-client-app")
client1 = SyncStealthApiClient(session=session)
client2 = SyncStealthApiClient(session=session)
```

Event Handling
==============

The client supports receiving asynchronous events from the Stealth server (e.g., chat messages, item updates).

`StealthEvent` - Represents an event with an `id` (EventType) and a list of `arguments`.

`get_event()` - Both async and sync clients provide this method to retrieve the next event from the queue.

Usage Examples
==============

### Asynchronous Example

```python
import asyncio
from py_astealth.api_client import AsyncStealthApiClient

async def main():
    client = AsyncStealthApiClient()
    await client.connect()
    
    # Call an API method
    self_id = await client.Self()
    print(f"My ID: {self_id}")
    
    # Event loop
    while True:
        event = await client.get_event()
        if event:
            print(f"Received event: {event}")
        await asyncio.sleep(0.1)

if __name__ == '__main__':
    asyncio.run(main())
```

### Synchronous Example

```python

from py_astealth.sync.sync_client import SyncStealthApiClient

# Using context manager for automatic connection/disconnection
with SyncStealthApiClient() as client:
    if client.Connected():
        print("Connected to Stealth!")

    client.AddToSystemJournal("Hello from Python!")
```

Code Generation
===============

The `py_astealth.generated` package contains auto-generated interface stubs (`AsyncInterface`, `SyncInterface`). 
These files are not meant to be edited manually but are crucial for providing IDE autocompletion and type hinting for the dynamically generated API methods.
