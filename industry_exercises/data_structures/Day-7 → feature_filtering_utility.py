def filter_features(features, allowed_features):
    # Convert allowed features to a set for fast lookup
    allowed_set = set(allowed_features)

    # Build feature-to-index mapping, preserving original indices
    feature_index = {
        name: idx
        for idx, name in enumerate(features)
        if name in allowed_set
    }

    return feature_index


# Test code (outside the function)
features = ["age", "salary", "experience", "city"]
allowed = ["age", "experience"]

filtered = filter_features(features, allowed)

print(filtered)