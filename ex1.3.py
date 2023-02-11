def fib2(n, cache = {}):                
    if n == 0 or n == 1:                        
        return n                                
    if n not in cache:                                       
        cache[n] = fib2(n-1, cache) + fib2(n-2, cache)
    return cache[n]

