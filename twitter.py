import tweepy
import twitter_auth


def lista_tweets(conta, last_tweet):
    api = twitter_auth.autentica_search()

    tweets = []

    for status in tweepy.Cursor(api.search, q="from:"+conta,  tweet_mode='extended', since_id=last_tweet, count=200).items():
        print(status)
        tweets.append(status)

    return tweets

def lista_tweets_old(conta):
    api = twitter_auth.autentica_first()

    tweets = []

    for status in tweepy.Cursor(api.user_timeline, id=conta,  tweet_mode='extended').items():
        tweets.append(status)

    return tweets


def get_all(conta):
    api = twitter_auth.autentica_first()

    tweets = []

    for status in tweepy.Cursor(api.search, q="from:"+conta,  tweet_mode='extended', count=200).items():
        tweets.append(status)

    return tweets


def tweet(handle, tweet, archive_url, creation_date, idTweets):
    api = twitter_auth.autentica_tweets()
    status = api.update_status("O tweet com id " + idTweets + " de " + creation_date + " sumiu da timeline da arroba " + handle + ", o tweet começava assim: ")
    tweet = str(tweet).replace("//", "/ /")
    status = api.update_status(in_reply_to_status_id = status.id, status = (tweet[0:200]+"..."))
    if not archive_url.startswith("Não"):
        api.update_status(in_reply_to_status_id = status.id, status = "Está arquivado nesse link: " + archive_url)


def insere_lista(arrobas):
    api = twitter_auth.autentica_list()

    for arroba in arrobas:
        try:
            user = api.get_user(screen_name=str(arroba))
            api.add_list_member(owner_screen_name="projeto7c0", slug="politicos-br", id=user.id)
        except:
            print("Erro com a arroba: " +arroba)


def list_tweets_list(topo):
    api = twitter_auth.autentica_list()

    tweets = []

    for status in tweepy.Cursor(api.list_timeline,tweet_mode='extended', owner_screen_name="projeto7c0", slug="politicos-br", since_id=topo, count=200).items():
        print(status)
        tweets.append(status)

    return tweets
