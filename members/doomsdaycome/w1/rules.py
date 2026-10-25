"""Module for checking thesis registration eligibility and missing requirements."""


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check if a student is eligible to register for a thesis.

    Args:
        credits: Total accumulated credits.
        gpa: Current grade point average.

    Returns:
        True if the student meets both credit and GPA requirements, False otherwise.
    """
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Determine the remaining requirements needed to register for a thesis.

    Args:
        credits: Total accumulated credits.
        gpa: Current grade point average.

    Returns:
        A list of strings detailing the missing credits or GPA.
    """
    result: list[str] = []

    if credits < 120:
        result.append(f"need {round(120 - credits, 1)} more credits")

    if gpa < 2.0:
        result.append(f"need {round(2.0 - gpa, 1)} more gpa")

    return result


if __name__ == "__main__":
    print(can_register_thesis(120, 2.0))
    print(missing(118, 3.1))
