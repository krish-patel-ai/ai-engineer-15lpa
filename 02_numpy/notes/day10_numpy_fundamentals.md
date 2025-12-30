NumPy is a numerical computing library in Python.

It is used for fast mathematical operations.

Python lists are slow for large numerical data.
NumPy uses arrays which store numbers in continuous memory.

NumPy supports vectorized operations.
Vectorization means operating on all elements without loops.

NumPy is the foundation of machine learning and deep learning.

To use NumPy, we import it using: import numpy as np.

np.array() is used to create NumPy arrays.
A NumPy array is different from a Python list.

The type of a NumPy array is numpy.ndarray.
NumPy arrays are used for efficient numerical computation.

# VECTORIZATION

Vectorization means applying operations to all elements at once.

NumPy allows element-wise operations without loops.
Example: array + 10 adds 10 to every element.

Vectorized operations are faster and cleaner than Python loops.
Vectorization is critical for machine learning performance.
Vectorization avoids Python loops.
NumPy performs element-wise operations internally in C.
This improves performance and reliability in ML systems.

# ARRAY TO ARRAY OPERATIONS
Array-to-array operations in NumPy are element-wise.
Both arrays must have compatible shapes.

Element-wise operations are used for feature weighting,
gradient updates, and loss calculations in ML. 

# BROADCASTING
Broadcasting allows NumPy to apply operations between arrays of different shapes.
It avoids loops and improves performance.
Broadcasting is commonly used for bias addition and scaling in ML pipelines.