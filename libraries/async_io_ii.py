# asyncio.ensure_future([future/coroutine], *, loop=None):
#   schedule execution of a future/coroutine
import asyncio

# Parallel execution of tasks

async def factorial(name, number):
    num = 1
    for i in range(2, number + 1):
        print("Task %s: Computing factorial(%s)..." % (name, i))
        num *= i
        await asyncio.sleep(1)
    print("Task %s DONE: factorial(%s) = %s" % (name, number, num))

loop = asyncio.get_event_loop()
# ensure_future([future/coroutine], loop=None):
#   1) schedule the execution of a coroutine object
#   2) wrap it in a future
#   3) return a Task object (a coroutine that is also a subclass of future)
# asyncio.gather(*[future/coroutine], loop=None, return_exceptions=False):
#   1) return a future aggregating results from the given futures/coroutine
#   2) if return_exceptions is true:
#        exceptions in the tasks are treated the same as successful results, and gathered in the result list
#        otherwise, the first raised exception will be immediately propagated to the returned future.
loop.run_until_complete(
    asyncio.gather(
        asyncio.ensure_future(factorial("A", 2)), # return a Task object 
        asyncio.ensure_future(factorial("B", 4)), # return a Task object
        asyncio.ensure_future(factorial("C", 8))  # return a Task object
    )
)
loop.close()

# Future Objects: class concurrent.futures.Future
# 1) done():
#    return True if the call was successfully cancelled or finished running
# 2) result(timeout=None):
#    return the value returned by the call
#    if the call hasn’t yet completed then this method will wait up to timeout seconds
#    if the call hasn’t completed in timeout seconds, then a TimeoutError will be raised
# 3) exception(timeout=None):
#    return the exception raised by the call
#    if the call hasn’t yet completed then this method will wait up to timeout seconds (default: no limit)
#    if the call hasn’t completed in timeout seconds, then a TimeoutError will be raised
# 4) add_done_callback(fn):
#    attaches the callable fn to the future
#    fn will be called, with the future as its only argument, when the future is cancelled or finishes running
