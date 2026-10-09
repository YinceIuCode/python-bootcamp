def can_register_thesis(credits : int, gpa : float) -> bool:
    return False if (credits < 120 or gpa < 2) else True

def missing(credits, gpa) -> list[str]:
    if can_register_thesis(credits, gpa):
        return ["Passed."]
    
    else:
        status = ""
        if credits < 120:
            status += f"Missing {120 - credits} credit(s)"
        
        if gpa < 2:
            status += "M" if status == "" else " and m"
            status += f"issing {round(2 - gpa, 2)} on gpa"
            
        status += "."
        
        return [status]

print(missing(120, 2))
print(missing(110, 2))
print(missing(110, 1.9))
print(missing(120, 1.9))