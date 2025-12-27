train_features = {"age", "salary"}
test_features = {"salary", "experience"}

all_features = train_features | test_features

print(all_features)