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

def tweet_start(handle):
    api = twitter_auth.autentica_tweets()
    status = api.update_status("Começando a listagem para a arroba " + handle + ". Sumiram desde a nossa última checagem:")
    return status

def tweet(handle, tweet, archive_url, creation_date, idTweets, status):
    api = twitter_auth.autentica_tweets()
    status = api.update_status(in_reply_to_status_id = status.id, status = "O tweet com id " + idTweets + " de " + creation_date + " que falava sobre: ")
    tweet = str(tweet).replace("//", "/ /")
    status = api.update_status(in_reply_to_status_id = status.id, status = (tweet[0:200]+"..."))
    if not archive_url.startswith("Não"):
        status = api.update_status(in_reply_to_status_id = status.id, status = "Está arquivado nesse link: " + archive_url)
    return status


def tweet_end(time, qtde_tweets):
    api = twitter_auth.autentica_tweets()
    status = api.update_status("Fim da triagem diária, foram encontrados " + str(qtde_tweets) + " tweets que sumiram, em " + str(time) +
                               " compartilhe o perfil @projeto7c0 para que mais " +
                               "pessoas saibam o que desaparece da timeline dos políticos.")
    status = api.update_status(in_reply_to_status_id = status.id, status = "Quer saber mais sobre o projeto? Acesse https://projeto7c0.com.br/ e veja saiba tudo sobre o projeto")
    status = api.update_status(in_reply_to_status_id = status.id, status = "Quer ajudar a financiar a transparência na comunicação da democracia brasileira? Acesse o nosso apoia-se em https://apoia.se/projeto-7c0 e veja como contribuir")
    api.update_status(in_reply_to_status_id = status.id, status = "Quer ficar atualizado? Assine a nossa newsletter, que teremos informações quinzenais para você! Para assinar só clicar aqui https://projeto7c0.us20.list-manage.com/subscribe/post?u=984470f280d60b82c247e3d7b&id=00a31b0d4a")

def insere_lista(arrobas):
    api = twitter_auth.autentica_list()

    for member in tweepy.Cursor(api.list_members, 'projeto7c0', 'politicos-br').items():
        try:
            arrobas.remove(member.screen_name)
        except:
            print("Não achei a arroba: " + member.screen_name)

    for arroba in arrobas:
        try:
            user = api.get_user(screen_name=str(arroba))
            api.add_list_member(owner_screen_name="projeto7c0", slug="politicos-br", id=user.id)
        except Exception as E:
            print("Erro com a arroba: " + arroba)
            print(E)


def list_tweets_list(topo):
    api = twitter_auth.autentica_list()

    tweets = []

    for status in tweepy.Cursor(api.list_timeline,tweet_mode='extended', owner_screen_name="projeto7c0", slug="politicos-br", since_id=topo, count=200).items():
        print(status)
        tweets.append(status)

    return tweets
