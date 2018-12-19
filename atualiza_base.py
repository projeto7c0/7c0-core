if __name__ == '__main__':
    import gevent.monkey
    import time
    import contas
    gevent.monkey.patch_all()
    import get_tweets
    from random import shuffle

    while True:
        arrobas = contas.pega_contas()
        # arrobas = ['renancalheiros']
        shuffle(arrobas)
        print("Colentado novos tweets...")
        start_time = time.time()
        get_tweets.get_new(arrobas)
        end_time = time.time()
        print(end_time-start_time)