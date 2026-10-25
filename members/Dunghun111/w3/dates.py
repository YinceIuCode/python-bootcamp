from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Manipulating due date from today."""
    splitted_dash = text.split("-")
    splitted_space = text.split(" ")
    
    valid_word = {
        "in" : 1,
        "next" : 1,
    }

    valid_word_unit = {
        "a" : 1
    }
    
    date_unit = {
        "day" : 1,
        "month" : 30,
        "year" : 365,
        "decade" : 3650,
        "century" : 36500,
        "millenium" : 365000
    }
    
    day_of_week = {
        "monday" : 0,
        "mon" : 0,
        "tuesday" : 1,
        "tue" : 1,
        "wednesday" : 2,
        "wed" : 2,
        "thursday" : 3,
        "thu" : 3,
        "friday" : 4,
        "fri" : 4,
        "saturday" : 5,
        "sat" : 5,
        "sunday" : 6,
        "sun" : 6    
    }
    
    if len(splitted_dash) == 3:
        due_date = date(int(splitted_dash[0]), int(splitted_dash[1]), int(splitted_dash[2]))
        
    elif len(splitted_space) == 1 and splitted_space[0].lower() == "tomorrow":
        due_date = today + timedelta(days=1)
                        
    elif len(splitted_space) == 3 and valid_word.get(splitted_space[0].lower()) != None:
        unit = splitted_space[2] if splitted_space[2][len(splitted_space[2]) - 1] != "s" else splitted_space[2][:-1]
        days_mult = int(splitted_space[1]) if splitted_space[1].isdigit() else -1
        days_mult = valid_word_unit[splitted_space[1]] if valid_word_unit.get(splitted_space[1]) != None else days_mult
        
        if date_unit.get(unit) == None or days_mult == -1:
            raise ValueError
        
        due_date = today + timedelta(days = days_mult * date_unit[unit])
    
    elif len(splitted_space) == 1 and day_of_week.get(splitted_space[0].lower()) != None:
        today_day_of_week = today.weekday()
        due_date = today + timedelta(days = 7 - abs(today_day_of_week - day_of_week[splitted_space[0].lower()]))
        
    else:
        raise ValueError
    
    return due_date

print(parse_due("Sat", date(2026, 10, 25)))