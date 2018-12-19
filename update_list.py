if __name__ == '__main__':
    import time
    import lists, contas

    arrobas = contas.pega_contas()

    print("Atualizando lista do projeto...")
    start_time = time.time()
    lists.atualiza_lista(arrobas)
    end_time = time.time()
    print(end_time-start_time)