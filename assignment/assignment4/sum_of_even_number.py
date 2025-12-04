def main():
    input_number = input("Enter a positive integer: ")
    try:
        number = int(input_number)
        if number == 0 or number == 1:
            print("Enter a integer greater than One.")
        elif number < 0:
            print("Please enter a positive integer.")
        else:
            result = sum_of_even_numbers(number)
            print(f"The sum of even numbers from 1 to {number} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def sum_of_even_numbers(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
    return total

main()