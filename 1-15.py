#### 1. Import the numpy package under the name `np` (★☆☆)
import numpy as np

#### 2. Print the numpy version and the configuration (★☆☆)
print("Exercise 2:")
print(np.__version__)
np.show_config()

#### 3. Create a null vector of size 10 (★☆☆)
nv = np.zeros(10)
print("Exercise 3 ")
print(nv)

#### 4. How to find the memory size of any array (★☆☆)
print("Exercise 4: " + str(nv.nbytes))

#### 5. How to get the documentation of the numpy add function from the command line? (★☆☆)
print("Exercise 5: python -m pydoc numpy.add")

#### 6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
nv = np.zeros(10)
nv[4] = 1
print("Exercise 6: " + str(nv))    

#### 7. Create a vector with values ranging from 10 to 49 (★☆☆)
nv1 = np.arange(10, 49)
print("Exercise 7:")
print(nv1)

#### 8. Reverse a vector (first element becomes last) (★☆☆)
print("Exercise 8:")
nv1 = nv1[::-1]
print(nv1)

#### 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
print("Exercise 9:")
mat = np.arange(9).reshape((3, 3))
print(mat)

#### 10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
print("Exercise 10:")
nv = np.array([1, 2, 0, 0, 4, 0])
print(np.where(nv == 0)[0])

#### 11. Create a 3x3 identity matrix (★☆☆)
print("Exercise 11:")
nv = np.identity(3)
print(nv)

#### 12. Create a 3x3x3 array with random values (★☆☆)
print("Exercise 12:")
nv = np.random.rand(3, 3, 3)
print(nv)

#### 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
print("Exercise 13:")
nv = np.random.rand(10, 10)
print(nv)
print(f"Minvalue: {np.min(nv)}\nMaxvalue: {np.max(nv)}")


#### 14. Create a random vector of size 30 and find the mean value (★☆☆)
print("Exercise 14:")
nv = np.random.rand(30)
print(nv)
print("Mean: " + str(np.mean(nv)))


#### 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
print("Exercise 15: ")
nv = np.ones((6, 6))
nv[1:-1, 1:-1] = 0
print(nv)