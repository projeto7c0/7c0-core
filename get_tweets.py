import twitter, database


def get_new(arrobas):
    for arroba in arrobas:
        print(arroba)
        last_tweet = database.get_last_id(arroba)
        tweets = twitter.lista_tweets(arroba, last_tweet)
        database.insere_lista(tweets)


def get_all(arrobas):
        for arroba in arrobas:
            print(arroba)
            try:
                tweets = twitter.lista_tweets_old(arroba)
            except:
                print("Erro na arroba: " + arroba)
            database.insere_lista(tweets)
