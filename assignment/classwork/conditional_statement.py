# grade = int(input("Enter your mrks:").strip())
# try:
#     if not grade:
#         raise ValueError("Empty input")
#     elif grade > 90:
#         print("A")
#     elif grade < 90 and grade >= 80:
#         print("B")
#     elif grade > 70 and grade <=80:
#         print("C")
#     elif grade <70 and grade >= 60:
#         print("D")
#     elif grade <60:
#         print("E")
#     else:
#         print("Invalid grade entered.")
# except ValueError as ve:
#     print(ve)

age = int(input("Enter your age:").strip())
if age < 20 or age > 13:
    print("Teenager")