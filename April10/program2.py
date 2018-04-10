# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 23:31:27 2018

@author: Sweet Home
"""

import numpy as np
twod_array = np.ndarray((2,4),dtype=int)

print("\nDimension of the array is",twod_array.shape)
twod_array.fill(1)


print("Original Contents of the 2d array:",twod_array)


threed_array = twod_array.reshape((2,2,2))
print("\nDimension of the new array is",threed_array.shape)

print("Original Contents of the 3d array:",threed_array)

threed_array +=5
print("\nAfter Adding 5 to each element")
print(threed_array)

threed_array -=2
print("\nAfter Subtracting 2 from each element")
print(threed_array)

threed_array *=5
print("\nAfter Multiplying 5 to each element")
print(threed_array)