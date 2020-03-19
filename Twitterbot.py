import time
import tweepy

class Tweeter:
	def Tweet(message):
		tweetmessage

def initaccount():
	auth = tweepy.OAuthHandler('','')
	auth.set_access_token('','')

	api = tweepy.API(auth)
	return api



api = initaccount()

while(1):
	t = Tweeter()
	date = time.strftime('%d:%m')
	clock = time.strftime('%H:%M')
	message = (clock+" "+date + " - Server status: online!")
	print(message)
	print("tweeting....")
	api.update_status(message)
	del t
	time.sleep(3600)