#Program that reads a file specified by the user, processes its contents, and then prints a sorted list of unique words or tokens found in the file.
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    var = line.split()
    for i in var:
        if not i in lst:
            lst.append(i)
lst.sort()
print(lst)
