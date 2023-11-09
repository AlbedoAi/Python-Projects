#If on linux use "#!/usr/bin/python3"

# Author: Shubham Raturi
# Details: To generate a random sequence from the entered range and pattern then find a reoccuring pattern in the sequence from the user input.
# Resources: https://www.cs.siue.edu/programming-style-guide

# randomness
import random

#main function which runs first before all the functions
def main():
    #array with the sequance
    sequanceArray = []
    add_size, seq_Length = inputFunc(sequanceArray)

    #joins the array together into a string to be
    bigstring = "".join(map(str, sequanceArray))

    #calls the function to print it by 100 char per line
    printByChar(bigstring, seq_Length, 0)

    #searches the sequence for the given pattern passes it to the function
    patterSearch(input("Enter pattern: "), bigstring, add_size, sequanceArray, seq_Length)

#takes input from the user and returns the inputed var's
def inputFunc(sequanceArray):
    seq_Length = int(input("Enter a length of random sequence(100 - 1024): "))

    #checks wether the length is within range
    if(seq_Length >= 100 and seq_Length <= 1024):
        add_size = int(input("Enter address size(4 or 8): "))
        if(add_size == 4 or add_size == 8):
            pattern_Choice = int(input("Choose one of the sequence pattern\n\t\t1. Llln\n\t\t2. Lnln\n\t\t3. nLnL\n\t\t4. nLLl\nEnter your choice: "))

            #generates the random sequance from the selected choices and length
            randomSeq(seq_Length, pattern_Choice, sequanceArray)
            return add_size, seq_Length
        else:
            print("Enter either 4 or 8")
    else:
        print("Enter in range of or equal to 100 - 1024 then followed by either 4 bytes of sequence to find or 8 bytes")

#fucntion which generates the random seqaunces to be used
def randomSeq(length, choice, sequanceArray):
    #the amount of times to run the for loop ex: 400/4 = run 100 times
    length = int(length/4)
    if(choice == 1):
        for x in range(length):
            sequanceArray += chr(random.randint(65, 90)) #uppercase
            sequanceArray += chr(random.randint(97, 122)) #lowercase
            sequanceArray += chr(random.randint(97, 122)) #lowercase
            sequanceArray += chr(random.randint(48, 57)) #number
    elif(choice == 2):
        for x in range(length):
            sequanceArray += chr(random.randint(65, 90)) #uppercase
            sequanceArray += chr(random.randint(48, 57)) #number
            sequanceArray += chr(random.randint(97, 122)) #lowercase
            sequanceArray += chr(random.randint(48, 57)) #number
    elif(choice == 3):
        for x in range(length):
            sequanceArray += chr(random.randint(48, 57)) #number
            sequanceArray += chr(random.randint(65, 90)) #uppercase
            sequanceArray += chr(random.randint(48, 57)) #number
            sequanceArray += chr(random.randint(65, 90)) #uppercase
    elif(choice == 4):
        for x in range(length):
            sequanceArray += chr(random.randint(48, 57)) #number
            sequanceArray += chr(random.randint(65, 90)) #uppercase
            sequanceArray += chr(random.randint(65, 90)) #uppercase
            sequanceArray += chr(random.randint(97, 122)) #lowercase
    return sequanceArray

#function to search for pattern in the sequance
def patterSearch(pattern, bigstring, add_size, seqArray, seq_Length):

    #stores the index in the array of the pattern
    arrayWithFoundIndex = []
    index = 0
    red = '\033[31m'
    normal = '\033[39m'
    patternLength = len(pattern)

    #while loop that runs for each the length of the sequance
    while index < len(bigstring):
        #finds the pattern and stores it
        index = bigstring.find(pattern, index)
        if index == -1:
            break
        print("Found at: ", index + 1)
        arrayWithFoundIndex.append(index)

        #skips the amount of lines due to the next few letter matching the pattern
        index += add_size

    #adds more space to the array as adding color messed it up
    newIndex = 0
    for x in range(len(arrayWithFoundIndex)):
        #inserts color to highlight the pattern
        seqArray.insert(arrayWithFoundIndex[x]+newIndex, red)
        seqArray.insert(arrayWithFoundIndex[x]+patternLength+1+newIndex, normal)
        newIndex += 2
    #joins the array together to be printed later
    dup_text = "".join(map(str, seqArray))
    #gets the changed size amount as adding ansii color codes adds more chars
    size = len(dup_text) - seq_Length

    #function to print by 100chars per line
    printByChar(dup_text, seq_Length, size)

#prints 100 char per line
def printByChar(dup_text, seq_Length, modifiedIndex):

    #sets the size to be printed modified index defines if the size changed
    chunk_size = 100 + modifiedIndex

    #divides the text by how much to print
    chunks = [dup_text[i:i+chunk_size] for i in range(0, seq_Length+modifiedIndex, chunk_size)]
    print("----------------------------------------------------------------------------------------------------\n\t\t Randomly Generated Sequence of len: {}\n----------------------------------------------------------------------------------------------------".format(seq_Length))
    #prints it by the format
    for chunk in chunks:
        print(chunk)
    print('\n')
    print("----------------------------------------------------------------------------------------------------")

# calls the main function to start the program
main()
