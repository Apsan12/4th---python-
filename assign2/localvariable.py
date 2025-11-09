x = 5

def change_variable():
    global x   # allows changing global variable
    print("Initial value of global variable:", x)
    x = 10     # modify global variable
    y = 20     # local variable
    print("Final value of global variable:", x)
    print("Local variable:", y)

# Call the function
change_variable()

# Global variable after function call
print("Global variable outside function:", x)
