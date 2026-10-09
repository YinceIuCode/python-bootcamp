def summary (scores: list[float]) -> dict:
    if not scores:
        raise ValueError("Empty list!")

    sorted_score = sorted(scores)
    n = len(scores)

    min_val = sorted_score[0]
    max_val = sorted_score[-1]

    mean_val = sum(sorted_score) / n

    mid = n // 2
    median_val = None

    if n & 1:
        median_val = sorted_score[mid]
    else:
        median_val = (sorted_score[mid - 1] + sorted_score[mid]) / 2

    return {
        "min" : round(min_val, 2),
        "max" : round(max_val,2),
        "mean" : round(mean_val,2),
        "median" : round(median_val, 2)
    }