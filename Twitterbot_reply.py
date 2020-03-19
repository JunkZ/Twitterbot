import time
import tweepy

class Tweeter:
        def Tweet(message):
                tweetmessage

def initaccount():
        auth = tweepy.OAuthHandler(','')
        auth.set_access_token('','')

        api = tweepy.API(auth)
        return api



api = initaccount()
lastid = api.mentions_timeline()[0].id
while(1):
        t = Tweeter()
        current = api.mentions_timeline()[0]
        currentid = current.id
        if (lastid != currentid):
           print("Found mention, replying...")
           lastid = currentid
           if (current.text == "@yourbot test"):
               api.update_status('Test confirmed!',currentid)
           elif (current.text == "@yourbot returnid"):
               api.update_status(('The id of your tweet is : ' + str(currentid)),currentid)
           elif (current.text == "@yourbot retweetthis"):
               api.retweet(currentid)
               api.update_status('Done!',currentid)
           elif (current.text == ("@yourbot hi" or "@yourbot hello" or "@yourbot Hi" or "@yourbot Hello")):
               api.update_status('hi :)',currentid)

        del t


        time.sleep(61)

