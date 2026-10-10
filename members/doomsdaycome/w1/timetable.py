def by_day(timetable: list[tuple[str, str]]) -> dict[str, list[str]]:
    result = {}

    for course, day in timetable:
        result.setdefault(day, []).append(course)

    for day, course in result.items():
        course.sort()

    return result


if __name__ == "__main__":
    print(by_day([("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]))
