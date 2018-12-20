if __name__ == '__main__':
    import time
    import lists
    import arquivar_tweets

    print("Colentado novos tweets...")
    start_time = time.time()
    lists.get_new_tweets()
    arquivar_tweets.arquivar_tweets()
    end_time = time.time()
