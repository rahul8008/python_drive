'''
while True:
    marks=int(input('enter ur marks:  '))
    if marks in range(90,101):
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
        print('invalid')
'''
'''
while True:
    num=int(input('enter number:  '))
    if num==0:
        print('equal')
    elif num>0:
        print('positive')
    elif num<0:
        print('negative')
    else:
        print('invalid')
'''


data = {}

while True:
    username = input("enter username : ")
    password = input("enter password : ")


    if username in data:
        print("Error: Data already exists!")
       
    else:
        data.update({username: password})
        print("current data:  ", data)

                    
