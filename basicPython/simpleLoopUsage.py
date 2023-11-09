#If on linux use "#!/usr/bin/python3"

# Author: Shubham Raturi
# Details: This simple program is made through the given flowchart.
# Resources: https://www.cs.siue.edu/programming-style-guide
while(True):
    number = int(input("Enter a number between or equal to 0 and 20: "))
    if(number >= 0 and number <=20):
        for x in range(number + 1):
                print("This is loop {:n}, your number sqaured is: ".format(x), x*x)
        break
