import re, time
import database_auth
import archiveis


def insere_um(tweet, db):
    cursor = db.cursor()

    try:
        line = re.sub('"', '', tweet.full_text)
        sql = "INSERT INTO `tweets`.`mimic_tweets` (`idTweets`, `plain_text`, `timestamp_tw`, `handle`, `retweets`, `favs`) VALUES (" \
              ""+tweet.id_str+", \""+ line +"\",\""+str(tweet.created_at)+"\" , \""+tweet.user.screen_name+"\", "+str(tweet.retweet_count)+", "+str(tweet.favorite_count)+\
              ");"
        try:
            cursor.execute(sql)
        except Exception as E:
            print(E)
    except Exception as E:
        print(E)


def insere_lista(tweets):
    db = database_auth.conecta_banco()
    for tweet in tweets:
        insere_um(tweet, db)
    db.commit()
    db.close()


def get_oldest_id(arroba):
    db = database_auth.conecta_banco()
    sql = "select min(idTweets) from mimic_tweets where handle = \""+arroba+"\";"
    cursor = db.cursor()
    value = ""
    try:
        cursor.execute(sql)
        value = cursor.fetchone()
    except Exception as E:
        print(E)
    db.close()
    return value[0]


def get_last_id(arroba):
    db = database_auth.conecta_banco()
    sql = "select max(idTweets) from mimic_tweets where handle = \""+arroba+"\";"
    cursor = db.cursor()
    value = ""
    try:
        cursor.execute(sql)
        value = cursor.fetchone()
    except Exception as E:
        print(E)
    db.close()
    return value[0]


def recupera_ids(conta):
    sql = "select idTweets from mimic_tweets where handle = \""+conta+"\" order by idTweets;"
    db = database_auth.conecta_banco()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        value = cursor.fetchall()
    except Exception as E:
        print(E)
    db.close()
    return value

def retrieve_tweet(twitter_url):
    tweet_id = twitter_url.split("/")[-1]
    # print(tweet_id)
    sql = "select * from mimic_tweets where idTweets = \"" + tweet_id + "\" and 7c0_tweeted = 0;"
    db = database_auth.conecta_banco()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        value = cursor.fetchone()
    except Exception as E:
        print(E)
    db.close()
    if value:
        if value[10]:
            return tweet_id, value[2], value[4], value[10], value[3]
        else:
            return tweet_id, value[2], value[4], "Não arquivado", value[3]
    else:
        return 0, "", "", "Não arquivado", ""

def update_tweet(id):
    sql = "update mimic_tweets set erased = 1, 7c0_tweeted = 1 where idTweets = \"" + id + "\";"
    db = database_auth.conecta_banco()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
    except Exception as E:
        print(E)
    db.commit()
    db.close()


def recupera_ids_sem_arquivo():
    sql = "select idTweets, handle from mimic_tweets where archive_url is null order by idTweets DESC limit 75"
    db = database_auth.conecta_banco()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        value = cursor.fetchall()
    except Exception as E:
        print(E)
    db.close()
    return value

def recupera_ids_sem_arquivo2():
    sql = "select idTweets, handle from mimic_tweets where archive_url is null order by idTweets DESC limit 5"
    db = database_auth.conecta_banco()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        value = cursor.fetchall()
    except Exception as E:
        print(E)
    db.close()
    return value


def adiciona_arquivo(id, url_arquivo):
    sql = "update mimic_tweets set archive_url =\""+url_arquivo+"\" where idTweets = \"" + str(id) + "\";"
    db = database_auth.conecta_banco()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
    except Exception as E:
        print(E)
    db.commit()
    db.close()


def recupera_ids_total():
    db = database_auth.conecta_banco()
    sql = "select max(idTweets) from mimic_tweets;"
    cursor = db.cursor()
    value = ""
    try:
        cursor.execute(sql)
        value = cursor.fetchone()
    except Exception as E:
        print(E)
    db.close()
    return value[0]
