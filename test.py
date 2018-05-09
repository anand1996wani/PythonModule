import List		#Import newly created list module for customizable list

print("Welcome To Customized Version Of Mylist")
new_list = None

while True:
	print("Enter Your Choice")	#User Choices
	print("1 : Create A New List Object")
	print("2 : Append Element")
	print("3 : Extend List")
	print("4 : Insert Element")
	print("5 : Pop Element")
	print("6 : Print Elements")
	print("7 : Exit")
	choice = input("\n")
	
	if choice=='1':
		print("Creating A New List Object")
		new_list = List.mylist()	#creating object
		datatypes = input("Enter The Datatypes To Be Inserted In Space Separated Format\n")
		datatypes = datatypes.split(" ")
		#print(datatypes)
		if(len(datatypes)==1):
			new_list.acceptOnly(datatypes)	#If single datatype
		else:
			new_list.acceptOnly(tuple(datatypes))	#If more than one datatype
	elif new_list!=None and choice=='2':
		print("Appending Element")
		temp = eval(input("Enter The Data To Be Appended\n"))
		#print(type(temp))
		new_list.append(temp)	#Append object function call
	elif new_list!=None and choice=='3':
		print("Extending List")
		temp = []
		num = int(input("Enter number of elements to be inserted\n"))
		while(num!=0):
			temp.append(eval(input()))
			num = num - 1
		new_list.extend(temp)	#Extend List Of Objects
	elif new_list!=None and choice=='4':
		print("Inserting Element")
		index = int(input("Enter The Index"))
		obj = eval(input("Enter The Object"))
		new_list.insert(index,obj)	#Insert at perticular location		
	elif new_list!=None and choice=='5':
		print("Poping Element")
		print("Poped Element Is",new_list.pop())	#Pop an object
	elif new_list!=None and choice=='6':
		new_list.printData()
	elif choice=='7':
		break
	else:
		print("Either wroing choice is entered or new list is not created")	
	print()
	
