from ast import Compare
import random
words = ['Prim', 'Brag', 'Heat', 'Celt', 'Tatu', 'Hawm', 'Like', 'Wark', 'Move']
correctWordHint = ["_", "_", "_", "_"]
def similarWords(a, b):
    randomWordSplit = list(a)
    userSplit = list(b)
    for x in range(len(randomWordSplit)):
        if randomWordSplit[x] == userSplit[x]:
            correctWordHint[x] = randomWordSplit[x]
        else:
            correctWordHint[x] = "_"
randomNum = random.randint(0, len(words)-1)
randomWord = words[randomNum]
# print(randomWord)

userInput = input("Enter a 4 letter word: ")
similarWords(randomWord, userInput)

while randomWord != userInput:
    if randomWord == userInput:
        print('You guessed correct!')
    elif randomWord != userInput:
        print('Incorrect you were close by: ' + (''.join(correctWordHint)))
        userInput = input("Enter a 4 letter word: ")
        similarWords(randomWord, userInput)
    else:
        print("Please enter appropriate length word")
print('You guessed correct!')