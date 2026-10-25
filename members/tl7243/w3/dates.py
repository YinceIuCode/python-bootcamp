from datetime import date, timedelta

def parse_due(text: str, today: date) -> date:

	"""Parse text into a date relative to today

    Supports ISO format (YYYY-MM-DD), 'today', 'tomorrow', 'in X day(s)', and weekday names
    """

	text2 = text.strip().lower()

	try:
		return date.fromisoformat(text2.strip())
	except ValueError:
		pass

	if text2 == "today":
		return today
	if text2 == "tomorrow":
		return today + timedelta(days=1)

	if text2.startswith("in ") and (text2.endswith(" days") or text2.endswith(" day")):
		if len(text2.split()) == 3 and text2.split()[1].isdigit():
			return today + timedelta(days=int(text2.split()[1]))

	weekdays = {
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
		"sunday": 6
	}
	if text2 in weekdays:
		days_ahead = (weekdays[text2]-today.weekday())%7
		if days_ahead <= 0:
			days_ahead += 7
		return today + timedelta(days=days_ahead)

	raise ValueError(f"Unknown date format: {text}")
