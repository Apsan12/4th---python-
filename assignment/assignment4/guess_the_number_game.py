import random


### Generates a random number between 1 and 100
numberToGuess = random.randint(1, 100)

print("Welcome to the Guess the Number Game!")
print("I have selected a number between 1 and 100.")
print("Can you guess what it is?")
    
while True:
    userGuess = input("Enter your guess (or type '-1' to quit): ")
        
    if userGuess.lower() == '-1':
            print("Thanks for playing! Goodbye!")
            isGuessCorrect = False
            break
        
    try:
        userGuess = int(userGuess)
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    ### Checks if the guess is correct or not and gives feedback
    if userGuess < -1 or userGuess > 100:
        print("Please enter a number between 1 and 100.")
        continue   
    elif userGuess != numberToGuess:
        print("Wrong Guess, Try again.")
    else:
        print(f"🎉 Correct!")
        playAgain = input("Do you want to play again? (yes/no): ")
        if playAgain.lower() != 'yes':
            print("Thanks for playing! Goodbye!")
            isGuessCorrect = False
            break