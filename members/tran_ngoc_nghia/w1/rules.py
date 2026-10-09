def can_register_thesis (credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0

def missing(credit: int, gpa: float) -> list[str]:
    result = []

    if credit < 120:
        result.append(f"Need {120 - credit} more credits")
    if gpa < 2.0:
        result.append(f"Need {2.0 - gpa} more gpa")

    return result

#testing 
credits = int(input("Enter your credits: "))
gpa = float(input("Enter your gpa: "))

if can_register_thesis(credits, gpa):
    print("You have registered thesis succesfully!")
else:
    print ("FAILED!")
    print(missing(credits, gpa))
    
    