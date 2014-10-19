import json
import urllib2

base = 'https://www.humblebundle.com/store/api/humblebundle?page_size=20&request=1'

defaultOptions = {
	"sort":'bestselling',
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


theURL = assembleURL(defaultOptions, base)

html = urllib2.urlopen(theURL)

temp = json.loads(html.read())

data = temp['results']