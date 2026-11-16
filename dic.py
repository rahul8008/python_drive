student={101:['vamsi','ece',2023,[1,2]],
         102:['manasa','mech',2022,[6,7]],
         103:['kamal','cse',2024,[1,2]],
         104:['siri','ece',2022,[4,5]],
         105:['ananth','cse',2023,[4,5]]
         }
info=int(input('enter admission number:'))
print(student.get(info))



'''d={101:"rana",
	102:"aha",
	103:"anu"
	}
print(d.get("abi"))
print(d.keys())
print(d.values())
print(d.items())
d.update({104:'abhi'})
print(d)
d.update({101:'ajay rana'})
print(d)
d.setdefault('105','rahul')
print(d)
d.setdefault('105','enos')
print(d)
print(d.popitem())'''
'''
for k in d:
	print(k,d[k])
for m,n in d.items():
	print(m,n)
a=[1,2,3,4,5,6]
val={i:i*2 for i in a}
print(val)
data = [1, 2, 2, 3]

# 1. List
[x * 10 for x in data]           # Output: [10, 20, 20, 30]

# 2. Tuple (via Generator)
tuple(x * 10 for x in data)      # Output: (10, 20, 20, 30)

# 3. Set
{x * 10 for x in data}           # Output: {10, 20, 30}

# 4. Dictionary
{x: x * 10 for x in data}        # Output: {1: 10, 2: 20, 3: 30}
'''
