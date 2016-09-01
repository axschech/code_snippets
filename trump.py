import requests
import urllib2

base_url = 'https://api.twitter.com/'
config = {
	'consumer_key': urllib2.quote('xcPk5b9zaw8Nex5217AVKenlq'),
	'consumer_secret': urllib2.quote('DQu8zn1ckINHEmTbkc7iJY5CRBB4SHBDQKIHqt3G427mBRoheF')
}

class BaseRequest:
	def __init__(self, base_url, resource, config):
		self.resource = base_url + resource
		self.config = config

	def buildString(self):
		string = self.config['consumer_key'] + ":" + self.config['consumer_secret']
		return string.encode('base64', 'strict')

	def buildHeader(self, data=None):
		authorization = data or self.buildString()
		authorization = 'Basic ' + authorization
		user_agent = 'Dat App'
		return {
			'Authorization': authorization,
			'User-Agent': user_agent
		}

class Auth(BaseRequest):
	def get(self):
		headers = self.buildHeader()
		headers['Authorization'] = headers['Authorization'].replace('\n', '')
		r = requests.post(self.resource, headers=headers, data={'grant_type': 'client_credentials'})
		response = r.json()
		headers['Authorization'] = 'Bearer ' + response['access_token']
		return headers
		

class Tweets(BaseRequest):
	def get(self, screen_name):
		r = requests.get(self.resource, params={'screen_name': screen_name, 'count': 200}, headers=self.config)
		return r.json()

class Count(BaseRequest):
	def get(self, screen_name):
		r = requests.get(self.resource, params={'screen_name': screen_name}, headers=self.config)
		return r.json()

auth = Auth(base_url, 'oauth2/token', config)
auth_obj = auth.get()

count = Count(base_url, '1.1/users/show.json', auth_obj)
count_obj = count.get('axschech')

print count_obj['statuses_count']

tweets = Tweets(base_url, '1.1/statuses/user_timeline.json', auth.get())
collection = tweets.get('axschech')
i = 0
try:
	print collection[1]['retweeted_status']
	print collection[1]['quoted_status']
except Exception, e:
	print str(e)
# for item in collection:
# 	i = i + 1
# 	print "\n" + str(i) + "\n"
# 	print "\n" + str(item['retweeted']) + "\n"
# 	print "\n" + item['text'] + "\n"