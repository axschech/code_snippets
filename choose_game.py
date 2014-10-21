import json
import urllib2
import random
import os.path
from platform import system
from time import time
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(" "+d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

base = 'https://www.humblebundle.com/store/api/humblebundle?page_size=20&request=1'

defaultOptions = {
	"sort":'alphabetical',
	"page": '0'
}


def assembleURL(options, toStr):
	try:
		url = str(toStr)
	except:
		return 0

	i = 1
	optionsLen = len(options)

	url = url + "&";
	for (key, val) in options.items():
		url = url + key + "=" + val
		if i != optionsLen:

			url = url + "&"
		i = i+1

	return url

def assembleData(url):

	curr_bot = [];
	curr_mid = [];
	curr_top = [];

	html = urllib2.urlopen(theURL)
	temp = json.loads(html.read())
	count = temp['num_pages']
	records = 0
	# print count
	if os.path.isfile('output.json'):
		handle = open('output.json','r');
		dataIn = json.loads(handle.read())
		handle.close()
		check = int(time())

		if count == dataIn['page_count'] and dataIn['time']>check:
			return dataIn

	for x in range(0, count):
		print "\n" + str(count - x) + " pages left.. \n"
		aURL = assembleURL({"sort":"alphabetical","page":str(x)},base);
		html = urllib2.urlopen(aURL)
		print aURL
		temp = json.loads(html.read())
		records = records + len(temp)
		for z in range(0, len(temp['results'])):

			obj = {
				"name":temp['results'][z]['human_name'],
				"description":temp['results'][z]['description'],
				"price":temp['results'][z]['current_price'][0],
				"platforms":temp['results'][z]['platforms']
			}
			if obj['price'] < 5.00:
				curr_bot.append(obj)
			elif obj['price'] > 5.00 and obj['price'] < 10.00:
				curr_mid.append(obj)
			else: 
				curr_top.append(obj)

			# data.append(obj)

			
	# print curr_bot
	# print "\n\n"
	# print curr_mid
	# print "\n\n"
	# print curr_top
	print "\n\n"
	print records
	print "\n\n"
	data = {
		"page_count":count,
		"count": records,
		"time": int(time())+86400,
		"low":curr_bot,
		"mid":curr_mid,
		"high":curr_top
	}

	print "\n Got data! \n"

	print "\n Writing data to file \n"

	handle = open('output.json','w');
	handle.write(json.dumps(data))
	handle.close()

	return data

def runQuiz(data):
	
	def randNum(length):
		return random.randint(0,length)

	def question(paramData,platform):
		
		test = 0

		while(test==0):
			index = randNum(len(paramData))
			# print paramData[index]
			if platform.lower() in paramData[index]['platforms']:
				test = 1
			else:
				del paramData[index]

		return paramData[index]
		# return paramData[index]		

	print "\n Trying to find your platform \n"
	os = system()
	if os == "Darwin":
		os = "Mac"
	print "\n Is your platform: " + os + "? \n"
	os_check = raw_input("\n Yes / No \n")

	try:
		str(os_check)
	except:
		print "\n That's not a choice! \n"
		return 0

	if os_check.lower()=="no" or os_check.lower()=="n":
		print "\n What is your platform? \n"
		os = raw_input("\n | 1: Windows | 2: Mac | 3: Linux | 4: Android | \n")
		try:
			os = int(os)
		except:
			print "That's not a number!"
			return 0

		if os < 1 or os > 4:
			print "\n That's not one of the choices \n"
			return 0
		if os == 1:
			os = "Windows"
		elif os == 2:
			os = "Mac"
		elif os == 3:
			os = "Linux"
		elif os == 4:
			os = "Android"

	print "\n How much do you want to spend? \n\n Chose one of the following \n"
	spend = raw_input("\n | 1: Under 5 dollars | 2: Between 5 and 10 dollars | 3: Over 10 dollars | \n")
	
	try:
		spend = int(spend)
	except:
		print "\n That's not a number! \n"
		return 0

	if spend < 1 or spend > 3:
		print "\n That's not one of the choices \n"
		return 0

	if spend == 1:
		ret = question(data['low'],os)
	elif spend == 2:
		ret = question(data['mid'],os)
	elif spend == 3:
		ret = question(data['high'], os)

	return ret

theURL = assembleURL(defaultOptions, base)
print "\n Getting data...\n"
data = assembleData(theURL)

print "\n Running Quiz\n"
test = 0
while test==0:
	quized = runQuiz(data)
	print "\n"+quized['name']+"\n"
	print "\n"+strip_tags(quized['description'])+"\n"
	if quized != 0:
		print "\n Do you like this game? \n"
		user_check = raw_input("\n Yes / No \n")

	try:
		str(user_check)
	except:
		print "\n That's not a choice! \n"

	if user_check.lower()!="no" and user_check.lower()!="n":
		test = 1


