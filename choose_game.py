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
	data = []
	html = urllib2.urlopen(theURL)
	temp = json.loads(html.read())
	count = temp['num_pages']
	print count

	data.append(temp['results'])

	for x in range(0, count):
		print "\n Getting page " + str(x) + "\n"
		html = urllib2.urlopen(theURL)
		temp = json.loads(html.read())
		data.append(temp['results'])

	print "\n Got data! \n"

	return data

theURL = assembleURL(defaultOptions, base)
print "\n Getting data...\n"
assembleData(theURL)