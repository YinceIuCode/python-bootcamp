from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Parse text into a date relative to today."""
    t = text.strip().lower()

    # 1. ISO format YYYY-MM-DD
    try:
        return date.fromisoformat(text.strip())
    except ValueError:
        pass

    # 2. "today" / "tomorrow"
    if t == "today":
        return today
    if t == "tomorrow":
        return today + timedelta(days=1)

    # 3. "in N days"
    if t.startswith("in ") and t.endswith(" days"):
        parts = t.split()
        if len(parts) == 3 and parts[1].isdigit():
            return today + timedelta(days=int(parts[1]))

    # 4. Weekday names (Mon, Tue, Wed, Thu, Fri, Sat, Sun)
    weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    if t in weekdays:
        target_weekday = weekdays.index(t)
        current_weekday = today.weekday()
        days_ahead = target_weekday - current_weekday
        if days_ahead <= 0:  # Next occurrence
            days_ahead += 7
        return today + timedelta(days=days_ahead)

    raise ValueError(f"Unknown date format: {text}")