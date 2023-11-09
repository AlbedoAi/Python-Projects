largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        fnum = float(num)
    except:
        print("Invalid input")
    if largest is None:
        largest = fnum
    elif largest < fnum:
        largest = fnum
    
    if smallest is None:
        smallest = fnum
    elif smallest > fnum:
        smallest = fnum
    if num == "done":
        break
    print(num)

print("Maximum is", largest)
print("Minimum is", smallest)