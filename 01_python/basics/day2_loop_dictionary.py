# Looping through dictionary

metrics = {
    "accuracy": 0.91,
    "precision": 0.88,
    "recall": 0.85
}

for metric in metrics:
    print(metric, metrics[metric])