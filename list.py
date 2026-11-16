from sys import getsizeof
a=[10,20,30,40,10,30]					#list ds (insertion order)(duplicates allowed)
									#(mutable->can change)(possible with indexing and slicing)
b={10,10,20,30,30,40,50}					#set ds(random order )(duplicates not allowed)
print(a)
print(b)
print(a[1])
a[1]=50
print(a)
print(getsizeof(a))
print(len(b))