scores = {
    "model_a": 0.91,
    "model_b": 0.72,
    "model_c": 0.88
}

high_scores = {name: score for name, score in scores.items() if score >= 0.85}

print(high_scores)