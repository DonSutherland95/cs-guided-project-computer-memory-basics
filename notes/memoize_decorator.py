import timeit  # library to time how long a function call takes
​
​
def memoize(func):
    """Reusable memoization decorator
​
    For any function that uses this decorator, that function will cache results here.
    When the decorated function gets called, if the parameters are already in the cache we can return
    the result from cache instead of re-computing.
    """
    cache = dict()
​
    def memoized_func(*args):
        if args in cache:
            return cache[args]
​
        result = func(*args)
        cache[args] = result
        return result
​
    return memoized_func
​
​
# Driver code to test memoize decorator
def fibonacci(n):
    """This fibonacci function will serve as an example of an expensive computation.
​
    Calculating the n-th Fibonacci in this fashion has O(2^n) time complexity — i.e., exponential time complexity.
    """
​
    if n == 0:
        return 0
​
    elif n == 1:
        return 1
​
    return fibonacci(n - 1) + fibonacci(n - 2)
​
​
# call fibonacci without memoization — this is roughly how long this call would take every time
# the fibonacci function is called with that number
print(timeit.timeit('fibonacci(35)', globals=globals(), number=1))  # -> 3.696307531
​
# memoize the function with our very simple cache-decorator
memoized_fibonacci = memoize(fibonacci)
​
# call memoized_fibonacci(50) for the first time
# remember: the parameter 50 is not in our cache yet for this function
print(timeit.timeit('memoized_fibonacci(35)', globals=globals(), number=1))  # -> 3.6484202909999994 (first call)
​
# call memoized_fibonacci(50) for the second time
# the argument 50 IS now in our cache along with its results.
# So we don't need to run fibonacci(35) again, just return the result associated with key 50 in our cache!
print(timeit.timeit('memoized_fibonacci(35)', globals=globals(), number=1))  # -> 1.5150000001185049e-06 (0.000001515 seconds)