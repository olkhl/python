hrs = input("Enter Hours:")
rate = input('Enter Rate:')
try:
    h = float(hrs)
    r = float(rate)
except:
    print("error")
    quit()
if h <= 40:
	pay = h * r
elif h > 40:
	pay = 1.5 * r *(h-40) + 40 * r
print('pay:', pay)
