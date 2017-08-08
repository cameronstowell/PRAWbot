import praw


# Provides a context from which to capture events that are passed to listeners
class EventCapturer:
    def __init__(self, bot):
        self.bot = bot

    def capture(self, listener):
        pass

    def __iadd__(self, listener):
        self.capture(listener)


class SubredditCapturer(EventCapturer):
    def __init__(self, bot, sr='all'):
        super().__init__(bot)
        self.subreddit = self.bot.subreddit(sr)

    def capture(self, listener):
        return self.subreddit


class UserCapturer(EventCapturer):
    def __init__(self, bot, user):
        super().__init__(bot)
        self.user = self.bot.redditor(user)


# Listeners parse through the captured events to find triggers
class EventListener:
    def __init__(self):
        self.capturers = []

    def add_capturer(self, capturer):
        self.capturers += capturer


class CommentListener(EventListener):
    pass


class SubmissionListener(EventListener):
    pass

