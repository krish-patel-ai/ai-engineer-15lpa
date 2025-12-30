import numpy as np

features = np.array([1000, 1500, 2000])
bias = 50

# Step 1: Add bias using broadcasting
# Step 2: Print original features
# Step 3: Print updated features
# Step 4: Explain in comments why broadcasting is preferred over loops
result=features*bias
print(features)
print(result)
# because loops are very slower in handling the large data and broadcasting is very faster and syntax friendly