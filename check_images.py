import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def some_job():
	#There are currently 3 verions for the nexus 9 wifi volantis

	check = 3

	r = requests.get('http://developers.google.com/android/nexus/images')

	soup = BeautifulSoup(r.text)

	stuff = soup.find(id="volantis").next_element
	links = stuff.next_element.next_element.find_all('a')

	print "\n" + str(datetime.now()) + "\n"

	if len(links) > check:
		f = open('log','a')
		f.write('Yes\n') # python will convert \n to os.linesep
		f.close() 
	else:
		f = open('log','a')
		f.write('No\n') # python will convert \n to os.linesep
		f.close() 

if __name__ == '__main__':
	some_job()
	sched = BlockingScheduler()
	sched.add_job(some_job, 'interval', minutes=60)
	try:
		sched.start()
	except (KeyboardInterrupt, SystemExit):
		pass