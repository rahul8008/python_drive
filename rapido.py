#rapido,uber:
#km?
##1-6 per km 5rs
##7-12 per km 6 rs
##13-20 per km 8 rs
##21-30 per km 10 rs
##greater than 30 -->ride not possible

##testcase:
##case1: 10 km
##amount: 30+24=54
##
##case2: 15km
##amount: 30+36+24 = 90
##km=float(input('enter your distance in km : '))
##    if km in range(1,7):
##        frst=km*5
##        print('your total amount is :',frst)
##    elif range(7,13):
##        sec=30+(km-6)*6
##        print('your total amount is :',sec)
##    elif range(13,21):
##        thr=66+(km-12)*8
##        print('your total amount is :',thr)
##    elif range(21,31):
##        four=122+(km-20)*10
##        print('your total amount is :',four)
##    else:
##        print('sorry we cant reachable our distance')
##Your code fails because elif range(7,13): always evaluates to True in
##Python, and range() only works with whole integers (not floats like 15.0 or 5.5).
##Because elif range(7,13): is always True, entering 15 triggers the second block
##30 + (15 - 6) * 6 = 84.0) instead of reaching the third block (66 + (15 - 12) * 8 = 90.0).
while True:
    km = float(input('enter your distance in km : '))
    if km <= 0:
        print('please enter a valid distance')
    elif km <= 6:
        frst = km * 5
        print('your total amount is :', frst)
    elif km <= 12:
        sec = 30 + (km - 6) * 6
        print('your total amount is :', sec)
    elif km <= 20:
        thr = 66 + (km - 12) * 8
        print('your total amount is :', thr)
    elif km <= 30:
        four = 130 + (km - 20) * 10
        print('your total amount is :', four)
    else:
        print('sorry we cant reachable our distance')




        

        
