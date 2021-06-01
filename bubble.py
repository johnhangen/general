# Bubble sort
#
# 6/1/2021
# @author Jack Hangen
# Complete
# Comparing big O of Bubble sort to actual

import numpy as np
import matplotlib.pyplot as plt

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


size = [10, 30, 50, 70, 100, 300, 500, 700, 1000, 3000, 5000, 7000, 10000]
comps = [] 
temp_array = [10 * 10, 30 * 30, 50 *50, 70 * 70, 100 * 100, 300 * 300, 500 *500, 700 * 700, 1000 * 1000, 3000 * 3000, 5000 *5000, 7000 * 7000, 10000 * 10000]

# runs the selection sort method for everything in the array size and stores it in comps
for i in size:
    array = np.random.randint(i, size = i)
    comp = bubbleSort(array)
    print(f"{i} number of comps: {comp}")
    comps.append(comp)

# Uses matplotlib to plot the algorithm efficiency
plt.plot(size, comps, 'r--', size, temp_array, 'b--')
plt.ylabel("Number of comparisons")
plt.xlabel("Size of array")
plt.title('bubble Sort Comparisons vs Big O')
plt.text(1000, 90000000, "red = bubble, blue = big O")
plt.axis([0, 10000,0,100000000])
plt.show()