print(help(set.union))

gandhiji={"pardhu","hari","ganesh","jyothi","aswitha","rahul"}
nehruji={"kamal","enos","chari","jyothi","aswitha","rahul"}

#union:----> all 
print(gandhiji.union(nehruji))
print(nehruji | gandhiji)


#intersection:----> commom 
print(gandhiji.intersection(nehruji))
print(nehruji & gandhiji)


#difference:
print(gandhiji.difference(nehruji))
print(nehruji-gandhiji)


#print(help(set.symmetric_difference))

print(gandhiji.symmetric_difference(nehruji))
print(nehruji ^ gandhiji)


#superset:
s1={1,2,3,4}
s2={1,2,3,4,5}
print(s1.issuperset(s2))
print(s1>=s2)


#subset:
print(s1.issubset(s2))
print(s1<=s2)


x={1,2,3,5}
y={4,5,6,5}
print(x.isdisjoint(y))
