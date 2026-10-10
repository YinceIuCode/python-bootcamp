def median(l: list[float]):
	l.sort()
	ln = len(l)
	return (l[ln//2]+l[ln//2-1])/2 if (ln % 2 == 0) else l[ln//2]

def summary(scores: list[float]) -> dict:
	return {
		"min" : round(min(scores),2),
		"max" : round(max(scores),2),
		"mean" : round(sum(scores)/len(scores),2),
		"median" : round(median(scores),2)
	}
