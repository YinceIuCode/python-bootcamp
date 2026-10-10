def by_day(timetable: list[tuple[str, str]]) -> dict[str, list[str]]:
	r = {}
	for c, d in timetable:
		r.setdefault(d,[]).append(c)
		r[d].sort()

	return r
