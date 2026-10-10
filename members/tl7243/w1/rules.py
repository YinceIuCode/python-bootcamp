def can_register_thesis(credits: int, gpa: float) -> bool:
	return credits >= 120 and gpa >= 2

def missing(credits: int, gpa: float) -> list[str]:
	s = "";

	if credits < 120:
		s = "need " + str(round(120 - credits, 1)) + " more credits"
		if gpa < 2:
			s += " and " + str(round(2 - gpa, 1)) + " more gpa"

	elif gpa < 2:
		s = "need " + str(round(2 - gpa, 1)) + " more gpa"

	return [s]
