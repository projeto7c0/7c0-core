if __name__ == '__main__':
    import database, contas
    import pandas as pd

    arrobas = contas.pega_contas()

    for arroba in arrobas:

        lista = database.list_apagados(arroba)

        print(lista)

        df = pd.DataFrame(list(lista), columns=["ids"])
        print(df)
        df.to_csv(r'/home/ec2-user/7c0-core/csv/tweets_deletados_de_'+arroba+'.csv')
