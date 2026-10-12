def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2


def missing(credits: int, gpa: float) -> list[str]:
    result = []

    if credits < 120:
        result.append(f"need {round(120 - credits, 1)} more credits")

    if gpa < 2:
        result.append(f"need {round(2 - gpa, 1)} more gpa")

    return result


if __name__ == "__main__":
    print(can_register_thesis(120, 2.0))
    print(missing(118, 3.1))
