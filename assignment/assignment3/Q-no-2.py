### Function to check whether the number is Positive or Negative.
### Returns true if Positive.
### Returns false if Negative.
def isPositive(num) -> bool:
    return num > 0

### Function to check whether the number is Even or Odd.
### Returns true if Even.
### Returns false if Odd.  
def isEven(num) -> bool:
    return num % 2 == 0
    
number = input("Enter a number:\t")
try:
    parsedNum = int(number)
    if(parsedNum == 0):
        print("The Number is Zero.")
    elif(isPositive(parsedNum) and isEven(parsedNum)):
        print("The number is a positive even number.")
    elif(isPositive(parsedNum) and not isEven(parsedNum)):
        print("The number is a positive odd number.")
    elif(not isPositive(parsedNum) and isEven(parsedNum)):
        print("The number is a negative even number.")
    elif(not isPositive(parsedNum) and not isEven(parsedNum)):
        print("The number is a negative odd number.")
except ValueError:
    print("Enter a valid number")
