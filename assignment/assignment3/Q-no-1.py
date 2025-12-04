greeting = input("Enter Greetings:\t")

if(greeting.split(' ')[0] == 'hello'):
    print("$0")
elif(greeting[0] == 'h'):
    print("$20")
else:
    print("$100")