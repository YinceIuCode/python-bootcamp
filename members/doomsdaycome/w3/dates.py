"""Module for parsing relative and absolute due dates."""

import re
from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Parse a due date string relative to a given reference date.

    Supports ISO format (YYYY-MM-DD), 'today', 'tomorrow', 'in X days',
    and full or abbreviated weekday names (calculating the next occurrence).

    Args:
        text: The text string representing the due date.
        today: The reference date used for relative calculations.

    Returns:
        The parsed date object.

    Raises:
        ValueError: If the text format is unrecognized or invalid.
    """
    cleaned_text = text.strip().lower()

    try:
        return date.fromisoformat(cleaned_text)
    except ValueError:
        pass

    if cleaned_text == "today":
        return today

    if cleaned_text == "tomorrow":
        return today + timedelta(days=1)

    match = re.fullmatch(r"in (\d+) days?", cleaned_text)

    if match:
        return today + timedelta(days=int(match.group(1)))

    weekdays = {
        "mon": 0,
        "monday": 0,
        "tue": 1,
        "tues": 1,
        "tuesday": 1,
        "wed": 2,
        "wednesday": 2,
        "thu": 3,
        "thur": 3,
        "thurs": 3,
        "thursday": 3,
        "fri": 4,
        "friday": 4,
        "sat": 5,
        "saturday": 5,
        "sun": 6,
        "sunday": 6,
    }

    if cleaned_text in weekdays:
        days_ahead = (weekdays[cleaned_text] - today.weekday()) % 7
        return today + timedelta(days=days_ahead or 7)

    raise ValueError(f"Unknown due date: {text!r}")
