score = input("Enter Score: ")
try:
    score69=float(score)
except:
    print('Try a number dumb!!')
    quit()
if score69 >= 1.0 or score69 < 0.0:
    print('Out of Range Dumb!!')
elif score69 >= 0.9:
    print('A')
elif score69 >= 0.8:
    print('B')
elif score69>=0.7:
    print('C')
elif score69>=0.6:
    print('D')
elif score69<0.6:
    print('F')
