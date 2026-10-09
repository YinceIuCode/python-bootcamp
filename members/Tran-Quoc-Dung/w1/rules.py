def can_register_thesis(credits : int, gpa : float) -> bool:
    return not (credits < 120 or gpa < 2)

def missing(credits, gpa) -> list[str]:
    if can_register_thesis(credits, gpa):
        return ["Passed."]
    
    else:
        status = ""
        if credits < 120:
            status += f"need {120 - credits} credits"
        
        if gpa < 2:
            status += "n" if status == "" else " and n"
            status += f"eed {round(2 - gpa, 2)} on gpa"
            
        status += "."
        
        return [status]

print(missing(120, 2))
print(missing(110, 2))
print(missing(110, 1.9))
print(missing(120, 1.9))