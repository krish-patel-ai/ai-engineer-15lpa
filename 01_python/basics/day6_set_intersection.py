train_ids = {1, 2, 3, 4}
test_ids = {4, 5, 6}

overlap = train_ids & test_ids

if overlap:
    print("Leakage detected:", overlap)
else:
    print("No leakage")