"""Module for organizing university timetables by day of the week."""


def by_day(timetable: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group a list of course-day tuples by day and sort the courses alphabetically.

    Args:
        timetable: A list of tuples containing (course_code, day).

    Returns:
        A dictionary mapping each day to a sorted list of course codes.
    """
    result: dict[str, list[str]] = {}

    for course, day in timetable:
        result.setdefault(day, []).append(course)

    for day, courses in result.items():
        courses.sort()

    return result


if __name__ == "__main__":
    print(by_day([("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]))
