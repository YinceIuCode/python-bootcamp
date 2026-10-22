from datetime import date, datetime, timedelta


def parse_due(text: str, today: date) -> date:
    """Parse a date string into a date object relative to today.

    Supports 'YYYY-MM-DD', 'tomorrow', 'in X days', and weekday names (e.g., 'Fri').
    """
    clean_text = text.strip().lower()

    if clean_text == "tomorrow":
        return today + timedelta(days=1)

    if clean_text.startswith("in ") and clean_text.endswith(" days"):
        try:
            days_str = clean_text[3:-5].strip()
            return today + timedelta(days=int(days_str))
        except ValueError as exc:
            raise ValueError(f"Invalid number of days in text: {text}") from exc

    try:
        return datetime.strptime(text.strip(), "%Y-%m-%d").date()
    except ValueError:
        pass

    weekdays: dict[str, int] = {
        "mon": 0, "monday": 0,
        "tue": 1, "tuesday": 1,
        "wed": 2, "wednesday": 2,
        "thu": 3, "thursday": 3,
        "fri": 4, "friday": 4,
        "sat": 5, "saturday": 5,
        "sun": 6, "sunday": 6,
    }
    if clean_text in weekdays:
        target_weekday: int = weekdays[clean_text]
        days_ahead: int = target_weekday - today.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown date format: {text}")