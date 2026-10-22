"""Module for analysing chat log latency statistics and route usage."""

import math
from collections import Counter, defaultdict
from typing import Any


def _percentile_95(values: list[float]) -> float:
    """Calculate 95th percentile using nearest rank method."""
    if not values:
        return 0.0
    sorted_v = sorted(values)
    k = math.ceil(0.95 * len(sorted_v)) - 1
    return float(sorted_v[max(0, k)])


def analyse(pairs: list[tuple[str, float]]) -> dict[str, Any]:
    """Analyse chat log route latencies to calculate counts, p95, and slowest route."""
    counts: Counter[str] = Counter()
    latencies: dict[str, list[float]] = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        latencies[route].append(latency)

    p95_dict: dict[str, float] = {
        route: _percentile_95(lats) for route, lats in latencies.items()
    }

    slowest_route: str | None = None
    if p95_dict:
        slowest_route = max(p95_dict, key=lambda k: p95_dict[k])

    return {
        "counts": dict(counts),
        "p95": p95_dict,
        "slowest": slowest_route,
    }