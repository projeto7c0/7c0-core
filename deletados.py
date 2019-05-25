if __name__ == '__main__':
    import gevent.monkey
    gevent.monkey.patch_all()
    import time
    import contas
    import verify_deletion
    from random import shuffle

    arrobas = contas.pega_contas()
    # arrobas = ["jairbolsonaro"]
    shuffle(arrobas)
    print("Checando se tweets foram removidos...")
    start_time = time.time()
    verify_deletion.verify(arrobas)
    end_time = time.time()
    print("Terminado em... ")
    print(end_time - start_time)

