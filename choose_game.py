import json
import urllib2

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

	data = []
	html = urllib2.urlopen(theURL)
	temp = json.loads(html.read())
	count = temp['num_pages']
	# print count

	for x in range(0, count):
		print "\n" + str(count - x) + " pages left.. \n"
		html = urllib2.urlopen(theURL)
		temp = json.loads(html.read())
		for z in range(0, len(temp['results'])):

			obj = {
				"name":temp['results'][z]['human_name'],
				"price":temp['results'][z]['current_price'][0],
				"platforms":temp['results'][z]['platforms']
			}
			data.append(obj)

	print "\n Got data! \n"

	return data

theURL = assembleURL(defaultOptions, base)
print "\n Getting data...\n"
data = assembleData(theURL)

print data[0]