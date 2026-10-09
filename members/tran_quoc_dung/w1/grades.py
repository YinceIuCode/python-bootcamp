def summary(scores: list[float]) -> dict: 
    import statistics
    
    if len(scores) <= 0: 
        raise ValueError()
    
    return {
        'min': min(scores), 
        'max' : max(scores), 
        'mean' : round(float(statistics.mean(scores)), 2), 
        'median' : round(float(statistics.median(scores)), 2)
    }

print(summary([7.5, 9, 6, 8]))
