import sys
import timeit
import matplotlib.pyplot as plt
import json

sys.setrecursionlimit(20000)
with open('Assignment-2/ex2.5.json', 'r') as inf:
    array = json.load(inf)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

times_list = [(timeit.timeit(lambda : func1(array[i], 0, len(array[i])-1), number= len(array))) for i in range(len(array))]

array_sizes = [len(array[j]) for j in range(len(array))]

print(times_list)
print(array_sizes)

plt.plot(array_sizes, times_list)
plt.ylabel('Time (s)')
plt.xlabel('Array Size')
plt.show()

