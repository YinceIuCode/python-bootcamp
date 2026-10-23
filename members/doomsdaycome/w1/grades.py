"""Module for computing statistical summaries of score lists."""

import statistics


def summary(scores: list[float]) -> dict[str, float]:
    """Compute summary statistics (min, max, mean, median) for a list of scores.

    Args:
        scores: A list of numerical scores.

    Returns:
        A dictionary containing rounded summary statistics.
    """
    return {
        "min": round(min(scores), 2),
        "max": round(max(scores), 2),
        "mean": round(statistics.mean(scores), 2),
        "median": round(statistics.median(scores), 2),
    }


if __name__ == "__main__":
    print(summary([7.5, 9.0, 6.0, 8.0]))
