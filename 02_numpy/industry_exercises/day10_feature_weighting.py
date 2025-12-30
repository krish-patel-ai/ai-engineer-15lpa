import numpy as np

features = np.array([100, 200, 300])
weights = np.array([0.1, 0.2, 0.3])

# Step 1: Apply element-wise multiplication
# Step 2: Print original features
# Step 3: Print weighted features
# Step 4: Explain (in comments) why this must be vectorized

ele_wise_mult=features*weights
print(features)
print(weights)
print(ele_wise_mult)
#because both feature and weights have same shape
