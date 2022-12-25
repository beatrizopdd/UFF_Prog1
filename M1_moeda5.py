moeda = [8, 8, 7, 8, 8]

if (moeda[0] + moeda[1] < moeda[2] + moeda[3]): # pesagem 1 
	if (moeda[0] < moeda[1]): # pesagem 2
		print("A moeda 1 é falsa!")
		
	elif (moeda[1] < moeda[0]): # pesagem 2
		print("A moeda 2 é falsa!")
		
elif (moeda[2] + moeda[3] < moeda[0] + moeda[1]): # pesagem 1
	if (moeda[2] < moeda[3]): # pesagem 2
		print("A moeda 3 é falsa!")
		
	elif (moeda[3] < moeda[2]): # pesagem 2
		print("A moeda 4 é falsa!")
		
elif (moeda[0] + moeda[1] == moeda[2] + moeda[3]): # pesagem 1
	print("A moeda 5 é falsa!")
