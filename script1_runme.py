import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

env_vars = {
    "reddit": {
        "client_id": os.getenv("REDDIT_CLIENT_ID"),
        "client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
        "password": os.getenv("REDDIT_PASSWORD"),
        "username": os.getenv("REDDIT_USERNAME"),
    },
}

online_access_configs = {
    "reddit": {
        "base": {
            "user_agent": "SmootCity:ResearchDept:Intern:V1 (by u/smoot_city)",
            **env_vars["reddit"],
        },
        "subreddits": {
            "milwaukee": [
                'milwaukee+wisconsin+WI',
                ('WEEnergies', 'we energies', 'WE Energies', 'WE Energy', 'we energy', 'we energ*','WE Energ*')
            ],
            "kolar": [
                "ClayBusters+TrapShooting+gun+guns+shotgun",
                ('k80', 'K-80', 'K80', 'R9', 'Kolar', 'kolar', 'klar', 'klr')
            ],
        },
    },
}

model_configs = {
    "doc2vec": {
        "min_count": 8,
    },
}

from src.connectme.reddit import smooter
from src.brainz import simple_thinker

mySmoot = smooter(online_access_configs).connect_now()
smootThinker = simple_thinker(model_configs).get_gensim_docvec_model()

print(f"initialized a smoot...their types: {type(mySmoot)} {type(smootThinker)}")
print(f"If all of this runs that means we're ready to start streaming data into a model via reddit scraper")

milwaukee_subreddit = mySmoot.subreddit(online_access_configs["reddit"]["subreddits"]["milwaukee"][0])
kolar_trapgun_subreddit = mySmoot.subreddit(online_access_configs["reddit"]["subreddits"]["kolar"][0])

for cf_tuple in [(milwaukee_subreddit, 'milwaukee'), (kolar_trapgun_subreddit, 'kolar')]:
    for comment in cf_tuple[0].comments(limit=None):
        for iter_item in online_access_configs["reddit"]["subreddits"][cf_tuple[1]][1]:
            if iter_item in comment.body:
                print(f"\n\ncomment: {comment.body}\n\n\n\n\n")  # print pretty