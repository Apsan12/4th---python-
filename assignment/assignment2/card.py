#Assignment 2: Question no.1

def make_card(name, age: int, message = "Have a good day.") -> str:
    if(not name):
        return "Please enter a valid name."
    elif(age <= 0):
        return "Please enter a valid age."
    return (f"Hello {name} ({age} years old)!\n{message}")

name = input("Enter your name:\t").strip()
age_input = input("Enter your age:\t").strip()
try:
    if(not age_input):
        print ("Age cannot be empty.")
    else:
        age = int(age_input)
        print(make_card(name, age))
except ValueError:
    print("Age must be a valid number!")