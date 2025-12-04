def main():
    input_day = input("Enter a day number (1-7): ")
    try:
        day_number = int(input_day)
        result = get_day(day_number)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")

def get_day(day_number):
   match(day_number):
        case 1:
           return "Monday" 
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day number. Please enter a number between 1 and 7." 

main()