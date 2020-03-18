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
	date = time.localtime(time.time())
	message = (str(date[2])+"/"+str(date[1])+" "+str(date[3])+":"+str(date[4]) + " - Server status: online!")
	print(message)
	print("tweeting....")
	api.update_status(message)
	del t
	time.sleep(60)