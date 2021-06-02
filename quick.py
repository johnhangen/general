# Quick sort
#
# 6/1/2021
# @author Jack Hangen
# Complete
# Comparing big O of suick sort to actual

import numpy as np
import matplotlib.pyplot as plt
import math

# method I stole for quick sort
def partition(array, start, end, comp):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            comp += 1
            high = high - 1

        while low <= high and array[low] <= pivot:
            comp += 1
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

# quick sort method
def quickSort(array, start, end, comp):
    comp = 0
    if start >= end: 
        return comp

    p = partition(array, start, end, comp)
    quickSort(array, start, p-1, comp)
    quickSort(array, p+1, end, comp)

size = [10, 30, 50, 70, 100, 300, 500, 700, 1000, 3000, 5000, 7000, 10000]
comps = []
temp_array = [10 * 10, 30 * 30, 50 *50, 70 * 70, 100 * 100, 300 * 300, 500 *500, 700 * 700, 1000 * 1000, 3000 * 3000, 5000 *5000, 7000 * 7000, 10000 * 10000]
comps = [] 
temp_array = [10 * math.log(10), 30 * math.log(30), 50 * math.log(50), 70 * math.log(70), 100 * math.log(100), 300 * math.log(300), 500 * math.log(500), 700 * math.log(700), 1000 * math.log(1000), 3000 * math.log(30000), 5000 * math.log(50000), 7000 * math.log(70000), 10000 * math.log(100000)]

for i in size:
    array = np.random.randint(i, size = i)
    comp = quickSort(array, 0, i - 1, 0)
    print(f"{i} number of comps: {comp}")
    comps.append(comp)

# runs the selection sort method for everything in the array size and stores it in comps

plt.plot(size, comps, 'r--', size, temp_array, 'b--')
plt.ylabel("Number of comparisons")
plt.xlabel("Size of array")
plt.title('Insertion Sort Comparisons vs Big O')
plt.text(1000, 90000000, "red = Insertion, blue = big O")
plt.show()   