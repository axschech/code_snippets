run = 1
notNum = 0
while(run):
	dat = raw_input("\nPlease give me a number\n")

	dat2 = raw_input("\nPlease give me another number\n")

	dat3 = raw_input("\nWhat should I do with those numbers? (add subtract multiply divide)\n")

	try:
		x,y = int(dat),int(dat2)
	except:
		print "Those are not numbers!";
		notNum = 1
		dat = ""

	if dat3!="":

		if dat3=="add":
			print x+y
		elif dat3=="subtract":
			print x-y
		elif dat3=="multiply":
			print x*y
		elif dat3=="divide":
			try:
				print x/y
			except ZeroDivisionError:
				print "Dividing by zero can cause the world to end!"

		else:
			print "I don't know what to do!"

		dat4 = raw_input("\n Are you done? y / n \n")
		if dat4 == "y":
			run = 0
	else:
		if(notNum!=1):
			print "Please enter an option"