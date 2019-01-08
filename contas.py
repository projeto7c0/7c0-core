import pandas as pd

def pega_contas():
    df = pd.read_csv("https://raw.githubusercontent.com/projeto7c0/redes-sociais-politicos/master/redes-sociais-politicos-full.csv")
    saved_column = df.Twitter
    saved_column.dropna(inplace=True)
    # print(saved_column)
    return saved_column.tolist()



