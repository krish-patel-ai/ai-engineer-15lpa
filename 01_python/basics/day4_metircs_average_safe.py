def evaluate_metrics(metrics):
    total=0
    count=0
    for name,value in metrics.items():
        print(f"{name}:{value}")
        total+=value
        if count==0:
            return None
    return total/count

metrics = {
    "accuracy": 0.91,
    "precision": 0.88,
    "recall": 0.85
}
a=evaluate_metrics(metrics)
print(a)