class mylist:
	data = None
	temp = None
	myList = None
	#data stores user given datatypes
	#temp = ['int','str','float']
	#temp indicates all valid pyton3 datatypes
	def __init__(self):
		self.data = []
		self.myList = []
		self.temp = ['int','str','float']
		
	#This function accepts datatypes which can be stored in the list 
	def acceptOnly(self,dataType):		
		if(type(dataType)==list):
			self.data.append(dataType[0])
			#print("Correct")
		elif(type(dataType)==tuple):
			for i in dataType:
				self.data.append(i)
			#print("Correct")
		else:
			print("Error acceptonly() function can only accept valid datatype or tuple of valid datatypes")
			print("Allowed datatypes are : ",self.temp)
		
		if self.data!=None:
			for i in self.data:
				if i not in self.temp:
					print("Error acceptonly() function can only accept valid datatype or tuple of valid datatypes")
					print("Allowed datatypes are : ",self.temp)

	#Appending a object to the existing list
	def append(self,element):
		#print(type(element))
		if type(element).__name__ not in self.data:
			print("Invalid datatype can not be appended")
			print("This list can on store ",self.data)
		else:
			self.myList.append(element)
			#print(self.myList)

	#Inserting a objects at a specfic location
	def insert(self,index,element):
		if type(element).__name__ not in self.data:
			print("Invalid datatype can not be appended")
			print("This list can on store ",self.data)
		else:
			self.myList.insert(index,element)
			#print(self.myList)

	#appending list of objects
	def extend(self,temp):	
		for i in temp:
			if type(i).__name__ not in self.data:
				print("Invalid datatype can not be appended")
				print("This list can on store ",self.data)
				break
		else:
			self.myList.extend(temp)
	
	#poping last element
	def pop(self):
		return self.myList.pop()
		
	#printData
	def printData(self):
		print("List Contains : ",self.myList)
		print()
