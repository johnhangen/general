# Merge sort
#
# 5/12/2021
# @author Jack Hangen
# Incomplete
# Comparing big O of Merge sort to actual

import numpy as np
import matplotlib.pyplot as plt


def mergeSort(arr):
    comp = 0
    if len(arr) > 1:
 
        mid = len(arr)//2
 
        L = arr[:mid]
 
        R = arr[mid:]
 
        mergeSort(L)
 
        mergeSort(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
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
temp_array = [10 * 10, 30 * 30, 50 *50, 70 * 70, 100 * 100, 300 * 300, 500 *500, 700 * 700, 1000 * 1000, 3000 * 3000, 5000 *5000, 7000 * 7000, 10000 * 10000]

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
plt.title('Insertion Sort Comparisons vs Big O')
plt.text(1000, 90000000, "red = Insertion, blue = big O")
plt.axis([0, 10000,0,100000000])
plt.show()   