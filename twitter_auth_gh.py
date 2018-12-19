import tweepy


def autentica_search():
    consumer_token = ''
    consumer_secret = ''
    key = ''
    secret = ''

    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(key, secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60,
                     retry_errors=set([503]))

    return api


def autentica_first():
    consumer_token = ''
    consumer_secret = ''
    key = ''
    secret = ''

    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(key, secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60,
                     retry_errors=set([503]))

    return api


def autentica_tweets():
    consumer_token = ''
    consumer_secret = ''
    key = ''
    secret = ''

    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(key, secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60,
                     retry_errors=set([503]))

    return api


def autentica_list():
    consumer_token = ''
    consumer_secret = ''
    key = ''
    secret = ''

    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(key, secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=60,
                     retry_errors=set([503]))

    return api
