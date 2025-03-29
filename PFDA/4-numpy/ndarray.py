# ndarray is a fast and flexible container for large datasets in Python 
# math operations on whole blocks of data using syntax similar to scalar elements. 

import numpy as np 
data = np.random.randn(2,3)
print("Original Dataset:","\n", "data = ", data, "\n")

# math operations 
print("Multiplication:", "\n", "data * 10 = ", data * 10, "\n")

# Remember, a ndarray is a generic multidimensional container for homogenous data; that is, all of the elements must be of the same type. Every array has a chape, a tuple indicating the size of each dimension, and a dtype, an object describing the data type of the array 

print("\nData Shape:\n", data.shape)
print("\nData Type:\n", data.dtype)

# create an array using the array function 
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)

print("\nCreating an array using `np.array()`\n", arr1)

# nested sequences, like a list of lists (equal length sub lists) will be converted into a multidimensional array. 
# check the number of dimensions of the array using ndim 

data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)

print("\nCreating a 2d array with a list of lists:\n", arr2)
print("\nDimensions using `.ndim`:\n", arr2.ndim)
print("\nArray 2 has shape:\n", arr2.shape)

# unless explicitly specified, np.array tries to infer a good data type for the array that it created. Stored in a special dtype metadata object. 
print("\nArray 2 has data type `.dtype`:\n", arr2.dtype)

print("\n`np.zeros` and `np.ones` create arrays of 0's or ones'.\n")
print("\nTo create a higher-dimensional array with these methods, pass a tuple\n")

# arange is an array-valued version of the built-in Python range function:
print("\nUsing `.arange` method is just like the python `range()` function, except it creates an array out of it")

# since NumPy is focused on numerical computing, the data type, if not specified, will in many cases be float64
# dtype is a special object containing the information the ndarray needs to interpret a chunk of memory as a particular type of data. 
    # They are a source of Numpys flexibility for interacting with data coming from other systems. 

print("\nExplicitly convert or 'cast' an array from one data type to another using `array.astype(type)` method.\n")

# if you cast float type to int type, the decimal will be truncated, no rounding 
# if you have an array of string(int) or string(float), you can use .astype to convert them to numeric form. 
    # if casting were to fail, a ValueError will be raised
    # when specifying a dtype for casting, you can also use another arrays .dtype attribute 
    
int_array = np.arange(10)
float_array = np.array([.22, .270, .357, .380, .44, .50], dtype = np.float64)

int_array = int_array.astype(float_array.dtype)
print("\nCast `int_array` to float using `float_array.dtype`:\n", "`int_array.astype(float_array.dtype)`\n")
print("Result:", "`int_array.dtype = `", int_array.dtype)

# ARITHMETIC WITH NUMPY ARRAYS 
print("ARITHMETIC")

print("Definition: Vectorization is the expression of batch operations on data without writing any for loops. Any arithmetic between equal sized arrays applies the operation element wise")


arr = np.array([[1., 2., 3.],[4., 5., 6.]])
mult = arr*arr
sub = arr-arr

print("\nStarting Array:\n", arr, "\nMultiply it by itself once:\n", mult, "\nSubtract it from itself once:\n", sub)

#Arithmetic operations with scalars propogate the scalar argument to each element in the array. 
print("\n1/arr will propogate the scalar argument to each element in the array:\n", 1/arr)






































