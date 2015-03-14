#There are currently 3 verions for the nexus 9 wifi volantis

check = 3

import requests
from bs4 import BeautifulSoup 

r = requests.get('http://developers.google.com/android/nexus/images')

soup = BeautifulSoup(r.text)

stuff = soup.find(id="volantis").next_element
links = stuff.next_element.next_element.find_all('a')

if len(links) > check:
	print "\nYes!\n"
else:
	print "\nNo!\n"