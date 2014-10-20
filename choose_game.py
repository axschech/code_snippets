import json
import urllib2
import os.path
from time import time

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
		html = urllib2.urlopen(theURL)
		temp = json.loads(html.read())
		records = records + len(temp)
		for z in range(0, len(temp['results'])):

			obj = {
				"name":temp['results'][z]['human_name'],
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

theURL = assembleURL(defaultOptions, base)
print "\n Getting data...\n"
data = assembleData(theURL)

print data['low'][0]