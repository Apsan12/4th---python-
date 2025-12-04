# Assignment 2: Question no.2
num_1 = 0

def display_num():
    num_2 = 10
    global num_1 
    print("Initial Golbal variable:", num_1)
    num_1 = 20
    print("Global variable:", num_1)
    print("Local variable:", num_2)

display_num()

