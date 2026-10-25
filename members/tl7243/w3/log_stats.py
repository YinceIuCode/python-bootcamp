import math
from collections import Counter
from typing import Any


def analyse(pairs: list[tuple[str, float | int]]) -> dict[str, Any]:

	"""Analyze route latencies and calculate counts, p95 and find the slowest route"""

	if not pairs:
		return {
			"counts": {},
			"p95": {},
			"slowest": None
		}

	counts = Counter(route for route, value in pairs)

	latencies: dict[str, list[float | int]] = {}
	for route, value in pairs:
		latencies.setdefault(route, []).append(value)

	p95: dict[str, float] = {
		route: sorted(value)[math.ceil(0.95 * len(value)) - 1]
		for route, value in latencies.items()
	}

	slowest = max(p95, key=lambda k: p95[k])

	return {
		"counts": dict(counts),
		"p95": p95,
		"slowest": slowest
	}
