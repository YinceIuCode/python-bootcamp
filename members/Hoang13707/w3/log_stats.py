import math
from collections import Counter, defaultdict


def _percentile_95(values: list[float]) -> float:
    """Calculate 95th percentile using nearest rank method."""
    if not values:
        return 0.0
    sorted_v = sorted(values)
    # 95th percentile index calculation
    k = math.ceil(0.95 * len(sorted_v)) - 1
    return float(sorted_v[max(0, k)])


def analyse(pairs: list[tuple[str, float]]) -> dict:
    """Analyse chat log route latencies."""
    counts = Counter()
    latencies = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        latencies[route].append(latency)

    p95_dict = {route: _percentile_95(lats) for route, lats in latencies.items()}

    slowest_route = None
    if p95_dict:
        slowest_route = max(p95_dict, key=p95_dict.get)

    return {
        "counts": dict(counts),
        "p95": p95_dict,
        "slowest": slowest_route,
    }