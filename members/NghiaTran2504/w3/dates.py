import re
from datetime import date, timedelta

WEEKDAYS = {
    "mon": 0, "monday": 0,
    "tue": 1, "tuesday": 1,
    "wed": 2, "wednesday": 2,
    "thu": 3, "thursday": 3,
    "fri": 4, "friday": 4,
    "sat": 5, "saturday": 5,
    "sun": 6, "sunday": 6
}

def parse_due(text:str, today: date) -> date:
    """Parse a date description string into a datetime.date object.

    Args:
        text: Date string representation (e.g., "2026-10-30", "tomorrow", "in 3 days", "Fri").
        today: The reference date to calculate relative offsets.

    Returns:
        The calculated absolute target date.

    Raises:
        ValueError: If the text format cannot be recognized.
    """
    
    text = text.strip().lower()
    try:
        return date.fromisoformat(text)
    except ValueError:
        pass

    if text == "tomorrow":
        return today + timedelta(days=1)

    match = re.match(r"^in\s(\d+)\s+days?$", text)
    if match:
        days = int(match.group(1))
        return today + timedelta(days)
    
    if text in WEEKDAYS:
        target_weekday = WEEKDAYS[text]
        days_ahead = (target_weekday - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7

        return today + timedelta(days_ahead);

    raise ValueError ("Invalid due date format!")

