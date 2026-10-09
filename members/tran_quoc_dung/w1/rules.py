def can_register_thesis(credits : int, gpa : float) -> bool:
    return not (credits < 120 or gpa < 2)

def missing(credits, gpa) -> list[str]:
    if can_register_thesis(credits, gpa):
        return []
    
    else:
        status_cre = ""
        status_gpa = ""
        if credits < 120:
            status_cre += f"need {120 - credits} more credits"
        
        if gpa < 2:
            status_gpa += f"need {2 - gpa} more gpa"
        
        return_list = []
        return_list.append(status_cre) if status_cre != "" else None
        return_list.append(status_gpa) if status_gpa != "" else None
        
        return return_list

print(missing(120, 2))
print(missing(110, 2))
print(missing(110, 1.9))
print(missing(120, 1.9))