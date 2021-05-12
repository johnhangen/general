# insertion sort
#
# 5/11/2021
# @author Jack Hangen
# Complete
# Comparing big O of insertion sort to actual


# imports
import numpy as np
import matplotlib.pyplot as plt

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

# Arrays set up
size = [10, 30, 50, 70, 100, 300, 500, 700, 1000, 3000, 5000, 7000, 10000]
comps = []
temp_array = [10 * 10, 30 * 30, 50 *50, 70 * 70, 100 * 100, 300 * 300, 500 *500, 700 * 700, 1000 * 1000, 3000 * 3000, 5000 *5000, 7000 * 7000, 10000 * 10000]

# runs the selection sort method for everything in the array size and stores it in comps
for i in size:
    array = np.random.randint(i, size = i)
    comp = insertionSort(array)
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