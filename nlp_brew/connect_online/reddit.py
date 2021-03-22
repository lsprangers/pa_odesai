import sys
from importlib import import_module

# TODO: @Luke_Sprangers --> Create DRY function to import stuff -- confused on how to make this simple.
libs_pure = ['praw', 'numpy', 'pandas']

for libname in libs_pure:
    try:
        lib = import_module(libname)
    except ImportError as e:
        print(f"{sys.exc_info()}")
    else:
        globals()[libname] = lib


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

    def connect_now(self):
        """connect to reddit"""

        return praw.Reddit(**self.reddit_login_configs["reddit"]["base"])
