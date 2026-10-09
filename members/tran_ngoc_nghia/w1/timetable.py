def by_day(course_days: list[tuple[str, str]]) -> dict[str, list[str]]:
    result = {}
    for course, day in course_days:
        result.setdefault(day, []).append(course)

    for day in result:
        result[day].sort()

    return result


# print(by_day([("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]))