if __name__ == '__main__':
    import time
    import lists
    import arquivar_tweets

    while True:
        print("Colentado novos tweets...")
        start_time = time.time()
        lists.get_new_tweets()
        arquivar_tweets.arquivar_tweets()
        end_time = time.time()
        print(end_time-start_time)
        if end_time-start_time<60:
            time.sleep(60 - (end_time - start_time))
