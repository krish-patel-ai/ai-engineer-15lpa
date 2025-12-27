def calculate_metrics():
    accuracy = 0.9
    precision = 0.85
    recall = 0.8

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall
    }


metrics = calculate_metrics()
print(metrics)