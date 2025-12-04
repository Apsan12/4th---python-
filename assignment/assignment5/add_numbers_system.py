import sys

if len(sys.argv) != 3:
    sys.exit("Please provide only two numbers to add.")

try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
except ValueError:
    sys.exit("Please provide valid numbers to add.")

result = num1 + num2

print(f"The sum of {num1} and {num2} is {result}")
