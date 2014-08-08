import random

def getChoices():
	choices = []
	def buildChoices():
		
		def getChoice():
		
			choice = raw_input("Please enter a choice\n")
			return choice

		choices.append(getChoice())
		if len(choices)>0:
			check = raw_input("Would you like to add another? Choose y/n")
			if(check=="y") :
				buildChoices()
		else :
			buildChoices()
		
		return choices

	return buildChoices()


def selectChoice(runs,choices):
	selects = choices
	stats = {}
	for z in range(0,len(selects)):
		print selects[z]
		stats[selects[z]] = 0
	
	for i in range(0,runs):

		num = random.randint(0,len(selects)-1)
		stats[selects[num]] = stats[selects[num]] + 1
		#print selects[num]	
	print str(stats)
	
def run():
	theInput = raw_input("How many times would you like to run? \n")
	theChoices = getChoices()
	
	try:
		inNum = int(theInput)

		selectChoice(inNum,theChoices)
	except:
		print "That is not a number!"
		run()
	

run()