def evaluate_metrics(metrics):
    # Step 1: None check
    if metrics is None:
        return None

    # Step 2: Type check
    if not isinstance(metrics, dict):
        return None

    # Step 3: Empty check
    if len(metrics) == 0:
        return None

    total = 0
    count = 0

    for value in metrics.values():
        total += value
        count += 1

    average = total / count

    return {
        "average": average,
        "count": count
    }


# Test code (outside the function)
metrics = {
    "accuracy": 0.91,
    "precision": 0.88,
    "recall": 0.85
}

result = evaluate_metrics(metrics)
print(result)