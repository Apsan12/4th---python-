num = int(input("Enter an integer: "))

if num == 0:
    print("The number is zero.")
elif num > 0:
    if num % 2 == 0:
        print("The number is a positive even number.")
    else:
        print("The number is a positive odd number.")
else:
    if num % 2 == 0:
        print("The number is a negative even number.")
    else:
        print("The number is a negative odd number.")