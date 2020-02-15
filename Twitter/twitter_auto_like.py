import tweepy
import time


auth = tweepy.OAuthHandler('','')
auth.set_access_token('','')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()


search = 'Javascript'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Like Tweet')
        tweet.favorite()
        time.sleep(10)
    except tweet.TweepError as e:
        print(e.reason)
    except StopIteration:
        break