'''n = int(input('enter random number: '))

if n in range(1, 21):
    print('complete')
else:
    print('out of range')
'''

'''
passw=input('enter password:')
if passw.isalpha() or passw.isnumeric():
    print('valid')

else:
    print('invalid')'''
'''
num=int(input('enter number:'))
if num%2==0 :
    print('even')
else:
    print('odd')
'''
'''
l=["pardhu","john","balayya","sampu"]
user=input()
if user not in l:
    print("valid")
    l.append(user)
    print(l)
    print("scuees")
else:
    print("invalid")
'''
while True:
    
    age=int(input("enter age:"))
    if age in range(6,13):
        print('child')
    elif age in range(13,19):
        print('teenage')
    elif age in range(19,26):
        print('youth')
    elif age>30:
        print('uncle')
    else:
        print('invalid age ')


