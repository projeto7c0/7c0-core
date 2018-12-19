import twitter


def compara(lista_antiga, lista_atual):
    ids_atuais = isola_ids(lista_atual)
    ids_antigos = corrige_lista(lista_antiga)

    ids_atuais = set(ids_atuais)
    ids_antigos = set(ids_antigos)

    diff = ids_antigos.difference(ids_atuais)
    print(diff)
    # twitter.tweet("O @lucaslago deletou os tweets com id: " + str(diff))


def isola_ids(tweets):
    ids = []
    for tweet in tweets:
        ids.append(int(tweet.id_str))
    return ids;


def corrige_lista(lista_antiga):
    ids_antigos = []
    for item in lista_antiga:
        ids_antigos.append(item[0])

    return ids_antigos