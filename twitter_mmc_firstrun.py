if __name__ == '__main__':
    import gevent.monkey
    gevent.monkey.patch_all()
    import get_tweets, contas
    from random import shuffle

    arrobas = contas.pega_contas()
    arrobas = ["SF_moro"]
    shuffle(arrobas)
    print("Colentado todos os tweets...")
    get_tweets.get_all(arrobas)
