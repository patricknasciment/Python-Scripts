import tweepy
import time


auth = tweepy.OAuthHandler('XS48xQjTWH5S3ruowbp9R3vYa','mM9LN7bzAmOIb1rSsX3vlU49YHZTukNei6FK8SiSNNsG9hzqIc')
auth.set_access_token('849606424216862720-EMm4UGxyZplqKxWwmRoUUKbJ2JMY39i','ALXfvnCkB9GviLUFReJgL7q6ndvzulhfVhhodNCIG1Jvs')

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