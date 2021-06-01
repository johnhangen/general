# Merge sort
#
# 6/1/2021
# @author Jack Hangen
# Complete
# Comparing big O of Merge sort to actual

import numpy as np
import matplotlib.pyplot as plt
import math

def mergeSort(arr):
    comp = 0
    comp += 1
    if len(arr) > 1:
 
        mid = len(arr)//2
 
        L = arr[:mid]
 
        R = arr[mid:]
 
        mergeSort(L)
 
        mergeSort(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            comp += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            comp += 1
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            comp += 1
            arr[k] = R[j]
            j += 1
            k += 1
    
    return comp


size = [10, 30, 50, 70, 100, 300, 500, 700, 1000, 3000, 5000, 7000, 10000]
comps = [] 
temp_array = [10 * math.log(10), 30 * math.log(30), 50 * math.log(50), 70 * math.log(70), 100 * math.log(100), 300 * math.log(300), 500 * math.log(500), 700 * math.log(700), 1000 * math.log(1000), 3000 * math.log(30000), 5000 * math.log(50000), 7000 * math.log(70000), 10000 * math.log(100000)]
print(math.log(300), math.log(500), math.log(700), math.log(1000))

# runs the selection sort method for everything in the array size and stores it in comps
for i in size:
    array = np.random.randint(i, size = i)
    comp = mergeSort(array)
    print(f"{i} number of comps: {comp}")
    comps.append(comp)

# Uses matplotlib to plot the algorithm efficiency
plt.plot(size, comps, 'r--', size, temp_array, 'b--')
plt.ylabel("Number of comparisons")
plt.xlabel("Size of array")
plt.title('mergeSort Sort Comparisons vs Big O')
plt.text(1000, 90000000, "red = mergeSort, blue = big O")
plt.show()