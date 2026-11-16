class Oops:
	def __init__(self,id,name,loc):
		self.id=id
		self.name=name
		self.loc=loc
	def details(self):
		print("my id :",self.id)
		print("my name :",self.name)
		print("my location:",self.loc)
		print()
o1=Oops(1,"dany","vizag")
o2=Oops(2,"reno","vizag")
o3=Oops(3,"meenu","vizag")
o1.details()
o2.details()
o3.details()