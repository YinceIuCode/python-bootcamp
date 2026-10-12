def by_day(schedule : list[tuple]) -> dict:
    schedule.sort(key = lambda event : event[0])
    
    timetable = {}

    for event in schedule:
        if (timetable.get(event[1]) == None):
            timetable.setdefault(event[1], [])
            
        timetable[event[1]].append(event[0])

    return timetable

print(by_day([("CSC100014", "Mon"), ("MTH100003", "Tue"), ("CSC100001", "Mon")]))
print(by_day([("CSC100024", "Mon"), ("MTH100053", "Tue"), ("CSC100067", "Mon"), ("CSC100019", "Fri")]))
print(by_day([("CSC110014", "Mon"), ("MTH120003", "Mon"), ("CSC130001", "Mon")]))
print(by_day([("CSC102014", "Mon"), ("MTH101003", "Tue"), ("CSC100301", "Mon"), ("MTH101003", "Sun")]))
print(by_day([("CSC100727", "Mon"), ("MTH100333", "Tue"), ("CSC100067", "Mon"), ("MTH100069", "Tue"), ("MTH100069", "Tue")]))