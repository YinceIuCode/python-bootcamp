"""Module for parsing due date strings into date objects."""

from datetime import date, timedelta

WEEKDAYS: dict[str, int] = {
    "mon": 0,
    "monday": 0,
    "tue": 1,
    "tuesday": 1,
    "wed": 2,
    "wednesday": 2,
    "thu": 3,
    "thursday": 3,
    "fri": 4,
    "friday": 4,
    "sat": 5,
    "saturday": 5,
    "sun": 6,
    "sunday": 6,
}


def parse_due(text: str, today: date | None = None) -> date:
    """Parse a due date string (ISO, 'tomorrow', 'in N days', or weekday) into a date."""
    if today is None:
        today = date.today()

    cleaned = text.strip()
    lowered = cleaned.lower()

    if not lowered:
        raise ValueError("Due date text cannot be empty.")

    if lowered == "today":
        return today
    if lowered == "tomorrow":
        return today + timedelta(days=1)

    if lowered.startswith("in ") and (
        lowered.endswith(" days") or lowered.endswith(" day")
    ):
        parts = lowered.split()
        if len(parts) == 3:
            try:
                days = int(parts[1])
                return today + timedelta(days=days)
            except ValueError as err:
                raise ValueError(f"Invalid day count in: '{text}'") from err

    if lowered in WEEKDAYS:
        target_wd = WEEKDAYS[lowered]
        days_ahead = (target_wd - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    try:
        return date.fromisoformat(cleaned)
    except ValueError as err:
        raise ValueError(f"Unknown due date format: '{text}'") from err