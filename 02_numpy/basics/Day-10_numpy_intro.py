import numpy as np
numbers=np.array([1,2,3,4])
print(numbers)

# vectorization

import numpy as np

np_array = np.array([1, 2, 3, 4])

new_array = np_array + 10

print(new_array)


# ---------- Exercise 1: Feature Weighting ----------
features = np.array([5, 10, 15])
weights = np.array([0.2, 0.3, 0.5])
weighted = features * weights
print(weighted)

# ---------- Exercise 2: Pipeline Safety ----------
print(features)
print(weights)
# Explanation in comments

# ---------- Exercise 3: Shape Mismatch ----------
a = np.array([1, 2, 3])
b = np.array([10, 20])
# print(a + b)   # uncomment to see error
# Explanation in comments


#BROADCASTING EXERCISE
features = np.array([1.2, 2.5, 3.8])
bias = 0.1

# Add bias using broadcasting
result=features+bias
print(result)

#EXERCISE 2

data = np.array([10, 20, 30])
scale = 2

# Multiply data using broadcasting
result=data*scale
print(result)

#NumPy Shapes & Dimensions (MAKE-OR-BREAK TOPIC)------------->
import numpy as np

a = np.array([10, 20, 30])
print(a)
print(a.shape)

#2D array 
b = np.array([[10, 20, 30]])
print(b)
print(b.shape)

#EXERCISE
x = np.array([5, 10, 15])
y = np.array([[5, 10, 15]])
z = np.array([[5], [10], [15]])

print(x.shape)
print(y.shape)
print(z.shape)

a = np.array([1, 2, 3])
b = np.array([[1], [2], [3]])
print(a.shape)
print(b.shape)

print(a * b)