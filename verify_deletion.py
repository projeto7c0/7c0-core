import database
import grequests
import twitter
import urllib.request


def exception_handler(request, exception):
    print(exception)


def verify(arrobas):

    for arroba in arrobas:
        urls = []
        print("Criando lista de links para... " + arroba)
        lista_antiga = database.recupera_ids(arroba)

        urls += ["https://twitter.com/" + arroba + "/status/" + str(id[0]) for id in lista_antiga]


        print("Verificando status dos links...")
        # print(len(urls))

        # urlss = [urls]

        if len(urls) > 500:
            urlss = split(urls, int(len(urls) / 500))
        else:
            urlss = [urls]

        for urls in urlss:
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
                        twitter.tweet(handle, tweet, archive_url, creation_date)
                        database.update_tweet(id)
                resp.close()



def check_status_code(url):
    code = urllib.request.urlopen(url).getcode()
    if code == 404:
        id, tweet, handle = database.retrieve_tweet(url)
        if len(tweet + handle) > 1:
            print(tweet)
            print(handle)
            print(url)
            twitter.tweet("O seguinte tweet sumiu da timeline do @" + handle + " -> " + tweet)
            database.update_tweet(id)

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))
