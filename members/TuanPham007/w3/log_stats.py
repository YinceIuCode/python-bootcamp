import math
from collections import Counter
from typing import Any


def _calculate_p95(latencies: list[float | int]) -> float:
    """Calculate the 95th percentile latency from a list of numeric values."""
    if not latencies:
        return 0.0
    sorted_latencies: list[float | int] = sorted(latencies)
    index: int = math.ceil(0.95 * len(sorted_latencies)) - 1
    index = max(0, min(index, len(sorted_latencies) - 1))
    return float(sorted_latencies[index])


def analyse(pairs: list[tuple[str, float | int]]) -> dict[str, Any]:
    """Analyze route latency pairs and return request counts, p95 latencies, and the slowest route."""
    if not pairs:
        return {"counts": {}, "p95": {}, "slowest": None}

    counts: Counter[str] = Counter(route for route, _ in pairs)

    route_latencies: dict[str, list[float | int]] = {}
    for route, latency in pairs:
        route_latencies.setdefault(route, []).append(latency)

    p95_dict: dict[str, float] = {
        route: _calculate_p95(latencies)
        for route, latencies in route_latencies.items()
    }

    slowest_route: str | None = (
        max(p95_dict, key=lambda r: p95_dict[r]) if p95_dict else None
    )

    return {
        "counts": dict(counts),
        "p95": p95_dict,
        "slowest": slowest_route,
    }