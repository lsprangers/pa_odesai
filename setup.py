import os
from dotenv import load_dotenv

import pandas as pd
import numpy as np
import gensim

load_dotenv(verbose=True)

env_vars = {
    "reddit": {
        "reddit_client_id": os.getenv("REDDIT_CLIENT_ID"),
        "reddit_client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
        "reddit_password": os.getenv("REDDIT_PASSWORD"),
        "reddit_username": os.getenv("REDDIT_USERNAME"),
    },
}

online_access_configs = {
    "reddit": {
        "base": {
            "user_agent": "SmootCity:ResearchDept:Intern:V1 (by u/smoot_city)",
            **env_vars["reddit"],
        }
    },
}

model_configs = {
    "doc2vec": {
        "min_count": 8,
    },
}

doc2vec_model = gensim.models.Doc2Vec(model_configs["doc2vec"])


t_configs = {
    "subreddit_groups": {
        "milwaukee": 'milwaukee+wisconsin+WI',
        "kolar": "ClayBusters+TrapShooting+gun+guns+shotgun",
    },
    "search_groups": {
        "milwaukee": ['WEEnergies', 'we energies', 'WE Energies', 'WE Energy', 'we energy', 'we energ*', 'WE Energ*'],
        "kolar": ['k80', 'K-80', 'K80', 'R9', 'Kolar', 'kolar', 'klar', 'klr'],
    }
}

milwaukee_subreddit = smootCityReddit.subreddit(t_configs["subreddit_groups"]["milwaukee"])
kolar_subreddit = smootCityReddit.subreddit(t_configs["subreddit_groups"]["kolar"])

for comment in kolar_subreddit.comments(limit=None):
    for iter_item in t_configs["search_groups"]["kolar"]:
        if iter_item in comment.body:
            print(f"comment: {comment.body}\n\n\n\n\n")     # print pretty


