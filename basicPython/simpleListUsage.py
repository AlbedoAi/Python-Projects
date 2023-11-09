#If on linux use "#!/usr/bin/python3"

# Details: This program just shows the basic immitation of the given program which just capitalizes the first name and last name also capitalizing the directory
# Resources: https://www.cs.siue.edu/programming-style-guide

mylist = [['kenny rogers', '/home/users/krogers'],
          ['tony robbins', '/home/trobbins'],
          ['johnny cash', '/home/users/jcash'],
          ['tito jackson', '/home/hut/tjackson'],
          ['tim tzuyu', '/home/users/ttzuyu'],
          ['kareena kapoor', '/home/users2/kkapoor']]
print("+------------------------------------------+")
print("|  ", str.title(mylist[0][0]), " |", mylist[0][1][0:12] + mylist[0][1][12:14].upper() + str.lower(mylist[0][1][14:]), "   |")
print("|  ", str.title(mylist[1][0]), " |  ", mylist[1][1][0:6] + str.upper(mylist[1][1][6:8]) + str.lower(mylist[1][1][8:]), "\t   |")
print("|  ", str.title(mylist[2][0]), "  | ", mylist[2][1][0:12] + str.upper(mylist[2][1][12:14]) + str.lower(mylist[2][1][14:]), "\t   |")
print("|  ", str.title(mylist[3][0]), " | ", mylist[3][1][0:10] + str.upper(mylist[3][1][10:12]) + str.lower(mylist[3][1][12:]), "   |")
print("|   ", str.title(mylist[4][0]), "   | ", mylist[4][1][0:12] + str.upper(mylist[4][1][12:14]) + str.lower(mylist[4][1][14:]), "   |")
print("| ", str.title(mylist[5][0]),"|", mylist[5][1][0:13] + str.upper(mylist[5][1][13:15]) + str.lower(mylist[5][1][15:]), "  |")
print("+------------------------------------------+")





