'''x=[10,20,30,40,50]
y=(10,20,30,40,50)
for i in range(len(x)):

    print(x[i],end=' ')
for i in range(len(y)):

    print(y[i],end=' ')
    '''
'''
x=[1,5,6,3,9,7,11,12]
for i in x:
    y=max(x)
    if i<=y:
        print(i)
'''

'''
x=[1,2,6,3,9,7,11,12]
y=[]
for i in range(len(x)):
    if i%2==0 and x[i]%2!=0:
        print(x[i],'even index odd value')
        y.append(x[i])
for i in range(len(x)):
    if i%2!=0 and x[i]%2!=0:
        print(x[i],'odd odd')
        y.append(x[i])
for i in range(len(x)):
    if i%2!=0 and x[i]%2==0:
        print(x[i],'odd even')
        y.append(x[i])
name=input('enter your name:  ').split(',')
print(name)
for i in range(len(name)):
    if i%2==0:
        print(name[i].upper(),end='')
        

'''

name=["a","b","c","d","e"]
for i in range(len(name)):
    if i==len(name[i]):
    print(name[i::-1])
    
