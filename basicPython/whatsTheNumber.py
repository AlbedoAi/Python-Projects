from ast import Import
import random

randomNum = random.randint(0,9) #Generates a random number

userInput = int(input("Enter a number between 0 and 9: ")) #Asks the user for an input and converts that input to an int

if userInput == randomNum: #If the input is correct it will print the result
    print("Correct")
else:
    while userInput != randomNum: #loops until the result is found
        userHint = userInput - randomNum
        print("You were close by: " + str(userHint))
        userInput = int(input("Enter a number between 0 and 9 again: "))
        if userInput == randomNum:
            print("Correct!")
        else:
            print("Incorrect")

        


