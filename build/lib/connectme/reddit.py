import praw


class smooter():

    def __init__(self, internet_configs):
        self.internet_configs = internet_configs

    def connect_now(self):
        return praw.Reddit(**self.internet_configs["reddit"]["base"])





