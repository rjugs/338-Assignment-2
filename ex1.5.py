import timeit
import matplotlib.pyplot as plt


def fib1(n):                        
    if n == 0 or n == 1:            
        return n                    
    else:                           
        return fib1(n-1) + fib1(n-2) 


def fib2(n, cache = {}):                
    if n == 0 or n == 1:                        
        return n                                
    if n not in cache:                                       
        cache[n] = fib2(n-1, cache) + fib2(n-2, cache)
    return cache[n]


n_list = [j for j in range(36)]

time_recursive_list = [(timeit.timeit(lambda : fib1(i), number=i)) for i in n_list]
time_memoization_list = [(timeit.timeit(lambda : fib2(i), number=i)) for i in n_list]

plt.plot(n_list, time_recursive_list, 'r', label = "Recursion")
plt.plot(n_list, time_memoization_list, 'b', label = "Memoization")
plt.xlabel("Values of n")
plt.ylabel("Time required to run function with n input (seconds)")
plt.title("Time Complexity of a Fibonacci function (Recursion vs. Memoization)")
plt.legend(loc= "upper left")
plt.show()


