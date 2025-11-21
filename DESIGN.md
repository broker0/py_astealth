Basic classes
=============

`ApiSpecification` is a base class used to declare APIs, `StealthApi` is its implementation, 
describing the UO Stealth Client API.

`AsyncRPCClient` - Client interface description. `AsyncStealthClient` is a concrete implementation 
of the UO Stealth Client RPC protocol.

`RPCType` - a base data type interface that provides methods for serialization and deserialization.
It implements serialization of lists (arrays) of identical elements.

`PrimitiveType` - a primitive data type representing only one value, 
implements serialization methods using the `struct` module.

`StructType` is a composite data type consisting of multiple value fields. 
Fields are serialized recursively if necessary.


Stealth related-classes
=======================

The `stealth_types.py` file describes the basic types used in the API, 
such as integers/floats, strings, and datetimes.

The file `stealth_structs.py` describes composite (structure) types.

`StealhApi` is a declarative description of the UO Stealth client API. 
It only requires declaring a function, annotating its arguments and return type, 
and using the `@ApiSpecification.method(int)` decorator to associate the method 
with its numeric identifier. 

Arguments and return values must inherit from `RPCType`.
For arrays, the notation `list[U8]`, `list[WorldPoint]` is used.

For example:

```py
class StealthApi(ApiSpecification):
    @ApiSpecification.method(14)
    def GetSelfID(self) -> U32: 
        pass

    @ApiSpecification.method(381)
    def GetMultiAllParts(self, MultiID: U32) -> list[MultiPart]:
        pass
```

`stealth_client.py` -

`AsyncStealthRPCProtocol` initially splits the received bytes into individual packets 
and passes them to the `AsyncRPCClient`, in this case `AsyncStealthClient`

`AsyncStealthClient` manages the connection to the UO Stealth Client 
and the reception and transmission of information about called functions 
and their results over this connection.

Method - `call_method` receives the method specification and its argument list, 
packs them into bytes, and sends them to the UO Stealth Client. 
It also waits for the method's execution result, if necessary, and decodes the result.

`api_client.py` -

`AsyncStealthApiClient` is an endpoint - it is a client and provides us with access to the API.
It inherits the `AsyncInterface` class and `AsyncStealthClient`. 
`AsyncInterface` is simply a stub with methods for IDE hints.

Method binding is performed by the `implement_api` decorator, which receives an `ApiSpecification`
class as an argument, describing the API, and a `method_factory` that simply returns a closure method 
that handles this call.
