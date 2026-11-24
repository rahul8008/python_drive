marks=int(input('enter ur marks'))
if marks in range(90,100):
    print('A')
elif marks in range(80,90):
    print('B')
elif marks in range(60,80):
    print('c')
elif marks in range(40,60):
    print('D')
elif marks<40:
    print('fail')
else:
    print(invalid)
