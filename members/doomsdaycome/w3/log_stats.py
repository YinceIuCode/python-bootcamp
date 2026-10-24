"""Module for analyzing network routing latencies and computing statistics."""

from collections import Counter
from math import ceil
from typing import Any


def analyse(pairs: list[tuple[str, float]]) -> dict[str, Any]:
    """Analyze route latency pairs to calculate frequency counts, p95 latencies, and identify the slowest route.

    Args:
        pairs: A list of tuples containing (route_name, latency_value).

    Returns:
        A dictionary containing occurrence counts, p95 latency values per route,
        and the name of the slowest route.
    """
    counts: Counter[str] = Counter()
    latencies: dict[str, list[float]] = {}

    for route, latency in pairs:
        counts[route] += 1
        latencies.setdefault(route, []).append(latency)

    p95 = {
        route: sorted(values)[ceil(0.95 * len(values)) - 1]
        for route, values in latencies.items()
    }

    slowest = max(p95, key=lambda route: p95[route], default=None)

    return {
        "counts": counts,
        "p95": p95,
        "slowest": slowest,
    }
