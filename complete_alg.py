# major sorting algos comparison
#
# 6/1/2021
# @author Jack Hangen
# imcomplete
# Comparing different sorting algorithums

import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import partition

# bubble Sort Method
def bubbleSort(arr):
  comp = 0
  n = len(arr)
  for i in range(n):
    comp += 1
    for j in range(0, n-i-1):
      comp += 1
      if arr[j] > arr[j+1] :
          arr[j], arr[j+1] = arr[j+1], arr[j]
  return comp

# Insertion Sort Method
def insertionSort(array):
    comp = 0
    for i in range(1, (len(array))):
        comp += 1
        while(array[i] < array[i - 1] | i - 1 != 0):
            comp += 1
            temp = array[i - 1]
            array[i - 1]= array[i]
            array[i] = temp
            i -= 1
    return comp

# Merge Sort Method
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

# selection sort method
def selection_Sort(array):
    current_min = 0
    current_item = 0
    comp = 0

    for i in range(len(array) - 1):
        current_min = array[i]
        comp += 1
        for i in range(current_item, len(array)):
            comp += 1
            if (array[i] < current_min):
                current_min = array[i]
                place = array[current_item]
                array[current_item] = array[i]
                array[i] = place

        current_item += 1
    return comp



size = [10, 30, 50, 70, 100, 300, 500, 700, 1000, 3000, 5000, 7000, 10000]
# runs the selection sort method for everything in the array size and stores it in comps

mcomps = []
for i in size:
    array = np.random.randint(i, size = i)
    comp = mergeSort(array)
    print(f"{i} number of comps: {comp}")
    mcomps.append(comp)

bcomps = []
for i in size:
    array = np.random.randint(i, size = i)
    comp = bubbleSort(array)
    print(f"{i} number of comps: {comp}")
    bcomps.append(comp)

icomps = []
for i in size:
    array = np.random.randint(i, size = i)
    comp = insertionSort(array)
    print(f"{i} number of comps: {comp}")
    icomps.append(comp)

scomps = []
for i in size:
    array = np.random.randint(i, size = i)
    comp = selection_Sort(array)
    print(f"{i} number of comps: {comp}")
    scomps.append(comp)

# Uses matplotlib to plot the algorithm efficiency
plt.plot(size, mcomps, 'r--', size, bcomps, 'b--', size, icomps, 'g--', size, scomps, 'y--', size)
plt.ylabel("Number of comparisons")
plt.xlabel("Size of array")
plt.title('All Sorting Methods')
plt.text(1000, 90000000, "Merge sort = Red, Bubble sort = Blue, Insertion sort = Green, Selection sort = Yellow")
plt.axis([0, 10000,0,100000000])
plt.show()   