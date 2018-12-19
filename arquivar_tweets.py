import gevent.monkey
import database
import archiveis
import savepagenow
import time

if __name__ == '__main__':
    gevent.monkey.patch_all()

    print("Arquivando tweets...")
    while True:
        lista_ids = database.recupera_ids_sem_arquivo()
        for par in lista_ids:
            url = "https://twitter.com/" + str(par[1]) + "/status/" + str(par[0])
            print(url)
            try:
                url_arquivo = archiveis.capture(url)
                database.adiciona_arquivo(par[0], url_arquivo)
            except Exception as E:
                print(E)
                print("Problema no arquivador principal")
                try:
                    url_arquivo = savepagenow.capture(url)
                    database.adiciona_arquivo(par[0], url_arquivo)
                    time.sleep(20)
                except Exception as E2:
                    print(E2)
                    print("Problema no arquivador reserva.")


def arquivar_tweets():
    print("Arquivando tweets...")
    lista_ids = database.recupera_ids_sem_arquivo2()
    for par in lista_ids:
        url = "https://twitter.com/" + str(par[1]) + "/status/" + str(par[0])
        print(url)
        try:
            url_arquivo = archiveis.capture(url)
            database.adiciona_arquivo(par[0], url_arquivo)
        except Exception as E:
            print(E)
            print("Problema no arquivador principal")
            try:
                url_arquivo = savepagenow.capture(url)
                database.adiciona_arquivo(par[0], url_arquivo)
                time.sleep(20)
            except Exception as E2:
                print(E2)
                print("Problema no arquivador reserva.")
