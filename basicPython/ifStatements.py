hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter Rate:")
r = float(rate)

if h > 40:
    oldPay = 40*10.5
    newRate = r*1.5
    newhrs = h-40
    pay = ((newRate*newhrs) + oldPay)
else:
    pay = h*r
print(pay)