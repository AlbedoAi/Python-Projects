from random import random
from turtle import xcor


randomWords = []

for x in range(3):
    randomWords.append(input("Enter a word: "))
print(randomWords)
print("The " + randomWords[1] + " to the left had a " + randomWords[0] +  " sign telling people to take the trail to the " + randomWords[2] + " This wasn't the way Zeke approached his hiking. ")
