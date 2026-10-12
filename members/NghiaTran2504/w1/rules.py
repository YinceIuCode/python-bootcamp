def can_register_thesis (credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0

def missing(credit: int, gpa: float) -> list[str]:
    result = []

    if credit < 120:
        result.append(f"need {120 - credit} more credits")
    if gpa < 2.0:
        result.append(f"need {2.0 - gpa} more gpa")

    return result

    
