#Create the following NumPy arrays:
#(a) float from 0.0 to 1.0 step 0.1, shape=(11,),
#(b) int zeros (1 byte) with shape=(5,6),
#(c) complex with shape=(9,), powers of x = complex(0, 1): 1, x, x**2, ..., x**8.

import numpy as np 


print(np.linspace(0, 1, 11))

print(np.zeros((5,6), dtype="int8"))

print(np.power(1J, np.arange(9)))

#(a) Create an arbitrary one dimensional array called v1.
#(b) Create a new array v2 which consists of the odd indices of v1.
#(c) Create a new array v3 in backwards ordering from v1.

import numpy as np

v1 = np.arange(10)
print(v1)
print(v1[1::2])
print(v1[::-1])

#(a) Create a two dimensional array called m1, shape=(4,5).
#(b) Create a new array m2 from m1, in which the elements of each row are in reverse order.
#(c) Create a new array m3 from m1, in which the elements of each column are in reverse order.
#(d) Cut of the first and last row and the first and last column of m1.

import numpy as np

m1 = np.arange(20).reshape(4,5)
print(m1)
print(m1[:,::-1])
print(m1[::-1,:])
print(m1[1:-1,1:-1])

