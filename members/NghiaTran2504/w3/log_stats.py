import math
from collections import Counter, defaultdict


def analyse(pairs: list[tuple[str, float | int]]) -> dict:
    """Analyze request counts, p95 latencies per route, and identify the slowest route.

    Args:
        pairs: List of tuples containing (route_name, latency_in_ms).

    Returns:
        A dictionary containing 'counts', 'p95', and 'slowest' route details.
    """
    
    if not pairs:
        return {"counts": Counter(), "p95": {}, "slowest": None}

    route_latencies = defaultdict(list)
    for route, latency in pairs:
        route_latencies[route].append(latency)

    counts = Counter()
    p95_dict = {}

    for route, lats in route_latencies.items():
        counts[route] = len(lats)
        sorted_lats = sorted(lats)
        n = len(sorted_lats)
        idx = max(0, math.ceil(0.95 * n) - 1)
        p95_dict[route] = sorted_lats[idx]

    slowest_route = max(p95_dict, key=p95_dict.get) # type: ignore

    return {
        "counts": counts,
        "p95": p95_dict,
        "slowest": slowest_route,
    }