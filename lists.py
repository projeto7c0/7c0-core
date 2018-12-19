import twitter
import database

def atualiza_lista(arrobas):
    twitter.insere_lista(arrobas)


def get_new_tweets():
    topo = database.recupera_ids_total()
    tweets = twitter.list_tweets_list(topo)
    database.insere_lista(tweets)