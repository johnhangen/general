# import numpy
import numpy as np

vecX = np.array = [1, 1]
vecY = np.array = [1, 1]

# Calculates the dot product
dot_product = np.dot(vecX, vecY)

# what does the dot product of the two vectors tell us
if(dot_product == 0):
    print("The angle between the two vectors is 90 degrees")
elif(dot_product == 1):
    print("The angle between the two vectors is 0 degrees")
elif(dot_product == -1):
    print("The angle between the two vectors is 180 degrees")
else:
    print("The angle between the two vectors is somthing other than 90 degrees")