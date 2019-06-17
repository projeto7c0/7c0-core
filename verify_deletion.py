import database
import grequests
import time
import twitter
from datetime import timedelta



def exception_handler(request, exception):
    print(exception)


def verify(arrobas):

    clock = time.monotonic()

    qtde_tweets = 0

    for arroba in arrobas:
        urls = []
        print(str(qtde_tweets) + " - criando lista de links para... " + arroba)
        lista_antiga = database.recupera_ids(arroba)

        urls += ["https://twitter.com/" + arroba + "/status/" + str(id[0]) for id in lista_antiga]


        print("Verificando status dos links...")

        if len(urls) > 20:
            urlss = split(urls, int(len(urls) / 20))
        else:
            urlss = [urls]

        for urls in urlss:
            time.sleep(5)
            try:
                requests = [grequests.get(url) for url in urls]
                responses = grequests.map(requests, exception_handler=exception_handler)
                # print(len(responses))

                for resp in responses:
                    if resp.status_code == 404:
                        id, tweet, handle, archive_url, creation_date = database.retrieve_tweet(resp.url)
                        if len(tweet + handle) > 1:
                            print(tweet)
                            print(handle)
                            print(resp.url)
                            print(archive_url)
                            twitter.tweet(handle, tweet, archive_url, creation_date, id)
                            qtde_tweets += 1
                            database.update_tweet(id)
                    resp.close()
            except Exception as E:
                print("erro... em alguma url")
                print(E)
                time.sleep(300)

    twitter.tweet_end(timedelta(seconds=time.monotonic() - clock), qtde_tweets)




def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))
