#If on linux use "#!/usr/bin/python3"

# Author: Shubham Raturi
# Details: This program just shows the basic immitation of the given program
# Resources: https://www.cs.siue.edu/programming-style-guide

int_var1 = [1,2,3,4]
str_var1 = "This is a string" #made the quotes the same
flt_var1 = '123.445'
tup_var1 = tuple(int_var1)

sumflt = flt_var1 # there is no 'int_var0'
sumflt = sumflt #+ int_var1 is a list so it doesnt work unless the element that you are trying to add is specified
#sumflt = sumflt + int_var2 no var2
#sumflt = sumflt + int_var3 no var 3

#tup_var1[0] = 2 it is immutable thus you arent able to edit or add to it after it been created

print("sumflt is: " + sumflt)
print(str_var1 + " " + flt_var1)
print("str_var1 * 4 " + str_var1 * 4)
#print("str_var1 + 4 " + str_var1 + 4) you cannot add str and int together

