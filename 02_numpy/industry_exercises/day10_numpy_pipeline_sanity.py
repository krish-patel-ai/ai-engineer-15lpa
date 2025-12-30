import numpy as np

# Raw numerical features (monthly income in rupees)
features = np.array([20000, 30000, 50000])

# Step 1: Convert rupees to thousands (vectorized)
features_thousands = features / 1000

# Step 2: Add bias of 2 using broadcasting
biased_features = features_thousands + 2

# Step 3: Convert to column vector (shape must be (3,1))
final_features = biased_features.reshape(-1, 1)

# Step 4: Print values and shapes at each step
print("Original:", features, features.shape)
print("Thousands:", features_thousands, features_thousands.shape)
print("Biased:", biased_features, biased_features.shape)
print("Final:", final_features, final_features.shape)

# Step 5: Explanation
# Shapes are checked at each step to avoid silent broadcasting bugs.
# Column vectors are required for ML matrix operations.
# Vectorization avoids Python loops and scales to large datasets.