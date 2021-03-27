import sys
import praw
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from dotenv import load_dotenv
import logging
import joblib

common_subreddits = {
    'energy': 'RenewableEnergy+hardenergy+energypolitics+oilandgasworkers+Oil+wisconsin+milwaukee',
    'dev': 'reddit_dev+code'
}


def print_attributes(pkg):
    the_attributes = [x for x in dir(pkg) if '__' not in x]  # ignore private vars
    print('attributes: \n')
    for att in the_attributes:
        print(str(att))


class SmootPraw:
    """class to connect to reddit via praw

    Args:
        reddit_login_configs (dict): dictionary containing reddit username, pass, clientID, and other configs
            necessary to connect to reddit via PRAW package

    Requires:
        praw() (import praw)

    """

    def __init__(self, reddit_login_configs):
        self.reddit_login_configs = reddit_login_configs
        self.reddit_instance = praw.Reddit(**self.reddit_login_configs)

    def get_common_subreddit(self, choice):
        return self.reddit_instance.subreddit(common_subreddits[choice])
