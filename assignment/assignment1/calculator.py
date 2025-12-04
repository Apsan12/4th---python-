def add(num1, num2):
    return num1 + num2
    
def sub(num1, num2):
    return num1 - num2
    
def multiply(num1, num2):
    return num1 * num2
    
def divide(num1, num2):
    if(num2 == 0):
        return "Cant divide by 0."
    return num1 / num2
    
def modulo(num1, num2):
    return num1 % num2
    
def power(num1, num2):
    return num1 ** num2
    
def floorDivision(num1, num2):
    if(num2 == 0):
        return "Cant divide by 0."
    return num1 // num2

isRepeat = True
while(isRepeat): 
    num1 = int(input("Please Enter your 1st number:\t"))
    num2 = int(input("Please Enter your 2st number:\t"))
    op = input("\nPlease enter the operator to perform calculation\nfor eg.\n+ for addition\n- for subtraction\n* for multiplication\n/ for division\n** for exponensiation\n// for floor division\noperator:\t")

    if(op == "+"):
        print(f"{num1}  {op}  {num2} = {add(num1, num2)}")
    elif(op == "-"):
        print(f"{num1}  {op}  {num2} = {sub(num1, num2)}")
    elif(op == "*"):
        print(f"{num1}  {op}  {num2} = {multiply(num1, num2)}")
    elif(op == "/"):
        if(num2 == 0):
            print(divide(num1, num2))
        else:
            print(f"{num1}  {op}  {num2} = {divide(num1, num2)}")
    elif(op == "%"):
        print(f"{num1}  {op}  {num2} = {modulo(num1, num2)}")
    elif(op == ""):
        print(f"{num1}  {op}  {num2} = {power(num1, num2)}")
    elif(op == "//"):
        if(num2 == 0):
            print(floorDivision(num1, num2))
        else:
            print(f"{num1}  {op}  {num2} = {floorDivision(num1, num2)}")
    else:
        #Error message if user enters an invalid operator
        print("Enter a valid operator")

    isRepeat = input("Do you want to perform another calculation? (yes/no): ").strip().lower() == "yes"