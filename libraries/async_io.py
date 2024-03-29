# asyncio:
# 1) create coroutines:
#    used when writing single-threaded concurrent code
# 2) use cases:
#    ex. multiplexing I/O access over sockets and other resources, and running network clients and servers, etc.
#
# coroutines and event loops:
# 1) what is coroutine:
#    it's like functions, but they can be suspended or resumed at certain points in the code
#      ex. pause a coroutine while it waits for an IO (or an HTTP request) and execute another one in the meantime
#    it's declarative:
#      i.e. call a coroutine function doesn't actually run them, but returns a coroutine object instead
# 2) how to actually execute a coroutine object
#    define another async (coroutine) function that awaits (or yield from) the coroutine object
#    (note: the coroutine object is returned by a native async (coroutine) function)
#    ex. async def async_func():
#            return await native_async_funct()
# 3) event loop:
#    used to orchestrate the execution of the coroutines
#    pass coroutine objects to an event loop to be executed later on
#    ex1. loop = asyncio.get_event_loop()
#         loop.run_until_complete(async_func())
#         loop.close()
#    ex2. loop = asyncio.get_event_loop()
#         tasks = [
#             asyncio.ensure_future(async_func(1)),
#             asyncio.ensure_future(async_func(2)),
#             asyncio.ensure_future(async_func(3))
#         ]
#         loop.run_until_complete(asyncio.gather(*tasks))
#         loop.close()

import asyncio

# two ways to define a coroutine function (effectively equivalent in type)
# 1) use async: (Python3.5+)
async def ping_server(ip):
    pass
# 2) use @asyncio.coroutine decorator: (Python3.4-)
@asyncio.coroutine
def load_file(path):
    pass

# coroutine methods:
# 1) asyncio.iscoroutinefunction(): determine if a function is a coroutine fucntion
print("Is coroutine: {}".format(asyncio.iscoroutinefunction(ping_server)))
print("Is coroutine: {}".format(asyncio.iscoroutinefunction(load_file)))
# 2) asyncio.iscoroutine(): determine if an object is a coroutine object
ping_server_obj = ping_server("1.1.1.1")
load_file_obj = load_file("/tmp/filename")
print("Is coroutine object: {}".format(asyncio.iscoroutine(ping_server_obj)))
print("Is coroutine object: {}".format(asyncio.iscoroutine(load_file_obj)))

# two ways to actually execute a coroutine function 
# 1) yield from:
#    yield control and wait for a coroutine object's completion
@asyncio.coroutine # function with yield function is typically decorated with the coroutine decorator
def get_json(client, url):  
    file_content = yield from load_file('/tmp/filename')
# 2) async/await: (primary syntax)
#    awaits releases the thread of execution (yield control to the caller) and wait for ping_server() completion
#    a) await a coroutine object's completion 
#    b) "async" is used to define a native coroutine function and "await" is used to "yield control" in place of "yeild from"
async def ping_local():  
    return await ping_server('192.168.1.1') # ping_server() must be awaitable, i.e. a coroutine

# event loop: the central execution device that provides
# 1) registering, executing and cancelling delayed calls (timeouts)
# 2) creating client and server transports for various kinds of communication
# 3) launching subprocesses and the associated transports for communication with an external program
# 4) delegating costly function calls to a pool of threads
print("event loop")
async def speak_async():  
    print('Hello asynchronicity!')
loop = asyncio.get_event_loop()          # get the default event loop 
loop.run_until_complete(speak_async())   # schedule and run the async task
                                         # (blocking: will not return until speak_async() is done)
loop.close()                             # close the event loop

