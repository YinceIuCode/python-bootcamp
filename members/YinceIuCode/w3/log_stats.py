"""Module for analysing chat route latencies and request counts."""

import math
from collections import Counter, defaultdict
from typing import Any


def analyse(pairs: list[tuple[str, int | float]]) -> dict[str, Any]:
    """Compute request counts, p95 latency per route, and the slowest route."""
    if not pairs:
        return {"counts": {}, "p95": {}, "slowest": None}

    counts: Counter[str] = Counter()
    latencies: defaultdict[str, list[int | float]] = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        latencies[route].append(latency)

    p95: dict[str, int | float] = {}
    for route, values in latencies.items():
        sorted_vals = sorted(values)
        idx = max(0, math.ceil(0.95 * len(sorted_vals)) - 1)
        p95[route] = sorted_vals[idx]

    slowest = max(p95, key=lambda r: p95[r])

    return {
        "counts": dict(counts),
        "p95": p95,
        "slowest": slowest,
    }