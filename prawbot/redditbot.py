import praw


class RedditBot:

    def __init__(self, client_id, client_secret, user_agent, username=None, password=None):
        self.reddit_instance = praw.Reddit(client_id, client_secret, password, user_agent, username)


def create_bot(client_id, client_secret, user_agent, username=None, password=None):
    return RedditBot(client_id, client_secret, user_agent, username, password).reddit_instance

