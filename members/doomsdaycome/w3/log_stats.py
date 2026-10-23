from collections import Counter
from math import ceil


def analyse(pairs) -> dict:
    counts = Counter()
    latencies = {}

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
