def by_day(schedule : list[tuple]) -> dict:
    schedule.sort(key = lambda event : event[0])
    
    timetable = {}

    for event in schedule:
        if (timetable.get(event[1]) == None):
            timetable.setdefault(event[1], [])
            
        timetable[event[1]].append(event[0])

    return timetable

print(by_day([("CSC100014", "Mon"), ("MTH100003", "Tue"), ("CSC100001", "Mon")]))