import os
import praw
from dotenv import load_dotenv
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
load_dotenv(verbose=True)

my_reddit_params = {
    'client_id': os.getenv("REDDIT_CLIENT_ID"),
    'client_secret': os.getenv("REDDIT_CLIENT_SECRET"),
    'username': os.getenv("REDDIT_USERNAME"),
    'password': os.getenv("REDDIT_PASSWORD"),
    'user_agent': "Checking:It:Out by (/smoot)",
}

common_subreddits = {
    'energy': 'RenewableEnergy+hardenergy+energypolitics+oilandgasworkers+Oil+wisconsin+milwaukee',
    'dev': 'reddit_dev+code',
    'vintage-clothes': 'vintagefashion+thriftstorehauls'
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

    def __init__(self, reddit_login_configs=my_reddit_params):
        self.reddit_login_configs = reddit_login_configs
        self.reddit_instance = praw.Reddit(**self.reddit_login_configs)

    def get_common_subreddit(self, choice):
        return self.reddit_instance.subreddit(common_subreddits[choice])


if __name__ == '__main__':
    tester = SmootPraw()
    tester_subr = tester.get_common_subreddit('energy')
    print(f"Got subreddit..type {type(tester_subr)}")
