import pymysql

def conecta_banco():
    address = ""
    user = ""
    passw = ""
    database = ""

    db = pymysql.connect(address, user, passw, database)
    return db
