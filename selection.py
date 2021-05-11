# Selection sort
#
# 5/11/2021
# @author Jack Hangen
# Complete
# Comparing big O of section to actual

import numpy as np
import matplotlib.pyplot as plt

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

# Arrays set up
size = [10, 30, 50, 70, 100, 300, 500, 700, 1000, 3000, 5000, 7000, 10000]
comps = []
temp_array = [10 * 10, 30 * 30, 50 *50, 70 * 70, 100 * 100, 300 * 300, 500 *500, 700 * 700, 1000 * 1000, 3000 * 3000, 5000 *5000, 7000 * 7000, 10000 * 10000]

# runs the selection sort method for everything in the array size and stores it in comps
for i in size:
    array = np.random.randint(i, size = i)
    comp = selection_Sort(array)
    print(f"{i} number of comps: {comp}")
    comps.append(comp)

# Uses matplotlib to plot the algorithm efficiency
plt.plot(size, comps, 'r--', size, temp_array, 'b--')
plt.ylabel("Number of comparisons")
plt.xlabel("Size of array")
plt.axis([0, 10000,0,100000000])
plt.show()      

