# from nlp_brew.connect_online import reddit

import sys
import os
import praw
from gensim.models.doc2vec import Doc2Vec
from dotenv import load_dotenv

load_dotenv(verbose=True)


my_kwargs = {
    'client_id': os.getenv("REDDIT_CLIENT_ID"),
    'client_secret': os.getenv("REDDIT_CLIENT_SECRET"),
    'username': os.getenv("REDDIT_USERNAME"),
    'password': os.getenv("REDDIT_PASSWORD"),
    'user_agent': "Checking:It:Out by (/smoot)",
}
rdt = praw.Reddit(**my_kwargs)

energy_list = "RenewableEnergy+hardenergy+energypolitics+oilandgasworkers+Oil+wisconsin+milwaukee"
comments = rdt.subreddit(energy_list).comments()

for _, comment in zip(range(1000), comments):
    print(comment.body, '\n', '-'*5)

print("DONE")
