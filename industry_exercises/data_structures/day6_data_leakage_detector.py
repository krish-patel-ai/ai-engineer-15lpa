def detect_data_leakage(train_ids, test_ids):
    # Convert input lists to sets to remove duplicates
    train_set = set(train_ids)
    test_set = set(test_ids)

    # Find overlapping IDs using set intersection
    overlap = train_set & test_set

    # Return the overlapping IDs (empty set if no leakage)
    return overlap


# Test code (outside the function)
train_ids = [1, 2, 3, 3, 5]
test_ids = [3, 5, 6, 7]

leakage = detect_data_leakage(train_ids, test_ids)

if leakage:
    print("Data leakage detected:", leakage)
else:
    print("No data leakage")