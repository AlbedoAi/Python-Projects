#If on linux use "#!/usr/bin/python3"

# Author: Shubham Raturi
# Details: This program uses a module to output all of the keywords with this language.
# Resources: https://www.cs.siue.edu/programming-style-guide
from keyword import kwlist
itemsInLine = 5

sortedList = sorted(kwlist, key=str.casefold) # sorts the list by ignoring uppercase
print("==================================================")
for x in range(0, len(kwlist), itemsInLine): #for loop that
    subList = sortedList[x:x+itemsInLine]
    line = '\t'.join(map(str, subList))
    print(line)
print("==================================================")

