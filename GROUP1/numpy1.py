import numpy as np

# Creating Arrays
# Create a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# Create a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# Create a 3D array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:\n", arr3)




# Array Operations
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

# Addition
sum_arr = arr1 + arr2
print("Sum:", sum_arr)

# Multiplication
product_arr = arr1 * arr2
print("Product:", product_arr)

# Exponentiation
exp_arr = arr1 ** 2
print("Exponentiation:", exp_arr)



# Matrix Operations
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Matrix multiplication
mat_mul = np.dot(arr1, arr2)
print("Matrix Multiplication:\n", mat_mul)

# Transpose of a matrix
transpose = arr1.T
print("Transpose:\n", transpose)



# Statisticial Operations
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Mean
mean = np.mean(arr)
print("Mean:", mean)

# Median
median = np.median(arr)
print("Median:", median)

# Standard Deviation
std_dev = np.std(arr)
print("Standard Deviation:", std_dev)


variance = np.var(arr)
print("Variation: ", variance)