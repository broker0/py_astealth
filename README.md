# py_astealth


Asynchronous/alternative python API for [UO Stealth client](https://stealth.od.ua/)

## Why?

### Speed

The original API implementation [py_stealth](https://github.com/ZeroDX255/py_stealth) isn't particularly fast. 
In the default configuration, it provides around 500 calls per second; 
after tuning, I was able to achieve just over 1,000 calls per second.

This implementation increases the number of calls per second by 3-5 times.


## Declarative Design

I tried to minimize the effort required to add new methods and types (structures) in the future.

We simply declare a new function, apply a decorator, annotate the arguments 
and return type ... and that's it!

Does the new function need a new data type? Declaring a structure is also a matter of 
a couple of decorators and type annotations.


### Flexibility

The original implementation provides a very simple interface - a module with functions that can be called from anywhere; 
the connection to the UO Stealth Client will be created automatically and transparently for the user, 
which is extremely convenient for simple scripts.

But, let's say, controlling several characters with one script is extremely difficult.

In this implementation, everything is at a lower level - you need to create a client object, 
connect to the UO Stealth Client and start working with it by calling functions.

Despite the additional complexity, the programmer has more options—for example, within a single script, 
multiple connections can be created for different characters and each can be controlled.

