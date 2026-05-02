def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1

        if n in cache:
            print(f"Taking from the cache: fib({n}) = {cache[n]}")
            return cache[n]

        print(f"Calculating for the first time fib({n})")
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

print(fib(10))  
print(fib(15)) 

print("---- Second function call ----")
print(fib(10))