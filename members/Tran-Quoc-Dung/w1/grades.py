def summary(scores: list[float]) -> dict: 
    import numpy
    return {} if len(scores) <= 0 else {
        'min': min(scores), 
        'max' : max(scores), 
        'mean' : round(float(numpy.mean(scores)), 2), 
        'median' : round(float(numpy.median(scores)), 2)
    }

print(summary([7.5, 9, 6, 8]))
print(summary([]))