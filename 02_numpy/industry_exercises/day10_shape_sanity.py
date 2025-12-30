import numpy as np

# Feature column vector
features = np.array([[100], [200], [300]])

# Weights column vector
weights = np.array([[0.1], [0.2], [0.3]])

print("Features shape:", features.shape)
print("Weights shape:", weights.shape)

# Explanation:
# Shapes must be checked to ensure correct alignment.
# Wrong shapes can cause broadcasting bugs or incorrect ML calculations.