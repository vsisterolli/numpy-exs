import numpy as np

#### 16. How to add a border (filled with 0's) around an existing array? (★☆☆)
print("Exercise 16:")
target = np.array([1, 2, 3, 4, 5])
final = np.zeros((3, target.size + 2))
final[1, 1:target.size + 1] = target
print(final)
# simply using .pad works as well
print(np.pad(target, 1))

#### 17. What is the result of the following expression? (★☆☆)
# 0 * np.nan     = nan
# np.nan == np.nan  = false
# np.inf > np.nan = false   
# np.nan - np.nan = np.nan
# np.nan in set([np.nan]) = false
# 0.3 == 3 * 0.1 = false

#### 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
print("Exercise 18:")   
mat = np.zeros((5, 5))
mat[1:5, 0:4] = np.diag([1, 2, 3, 4])
print(mat)

#### 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
print("Exercise 19:")   
checkpat = np.zeros(9)
checkpat[::2] = 1
mat = np.array([checkpat[0:8]] * 8)
mat[1::2] = checkpat[1:9]
print(mat)

#### 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element? (★☆☆)
# 1 * 7 * 8 = 56 so x = 2, since we want to advance more than 56 elements and less than 112
# 5 * 8 = 40, so y = 6 since we want to advance more than 4 ellements and less than 8
# z = 4
# 0-indexing, 1, 5, 3
print("Exercise 20:") 
print("x = 1, y = 5, z = 3")
# Just for confirmation
print(np.unravel_index(99, (6, 7, 8)))

#### 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)
print("Exercise 21:") 
print(np.tile(np.array([[1, 0], [0, 1]]), (4, 4)))

#### 22. Normalize a 5x5 random matrix (★☆☆)
print("Exercise 22:") 
mat = np.random.rand(5, 5)
det = np.linalg.det(mat)
print(mat / det)

#### 23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)
print("Exercise 23:") 
rgbaT = np.dtype({
    'names': ['r', 'g', 'b', 'a'],
    'formats': [np.ubyte, np.ubyte, np.ubyte, np.ubyte]
})
print(rgbaT)

#### 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
print("Exercise 24:") 
mat1 = np.random.rand(5, 3)
mat2 = np.random.rand(3, 2)
print(mat1 @ mat2)

#### 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)
print("Exercise 25:") 
v = np.arange(10)
v[(v >= 3) & (v <= 8)] *= -1
print(v)

#### 26. What is the output of the following script? (★☆☆)
# Author: Jake VanderPlas 
# print(sum(range(5),-1)) -> 9 because its summing all numbers from 0 to 4 and -1
# from numpy import *
# print(sum(range(5),-1)) -> 10 because its summing all numbers of the vector produced by range [0, 4] on the last axis (there is just one)

#### 27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)
# Z**Z / legal, just element by element expo 
# 2 << Z >> 2 / legal, just bitwise operations (leftshift 2x then rightshift 2x)
# Z <- Z / legal, number by number comparison
# 1j*Z / legal, 1j is the imaginary unity
# Z/1/1 / legal, just division by one
# Z<Z>Z / ilegal

#### 28. What are the result of the following expressions? (★☆☆)
# np.array(0) / np.array(0) -> error because of 0 division, returns nan
# np.array(0) // np.array(0) -> still error, but now returns 0 (nan-safe)
# np.array([np.nan]).astype(int).astype(float) -> error, nan is not a number and cant be converted, return -infinite

#### 29. How to round away from zero a float array ? (★☆☆)
# use the ceil function
print("Exercise 29: ")
v = np.random.rand(10)
v = np.ceil(v)
print(v)

#### 30. How to find common values between two arrays? (★☆☆)
print("Exercise 30: ")
x = np.arange(1, 10)
y = np.arange(5, 20)
print(np.intersect1d(x, y))