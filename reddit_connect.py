import praw
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

smootCityReddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    password=os.getenv("REDDIT_PASSWORD"),
    username=os.getenv("REDDIT_USERNAME"),
    user_agent="SmootCity:ResearchDept:Intern:V1 (by u/smoot_city)",
)

t_configs = {
    "subreddit_groups": {
        "milwaukee": ['milwaukee+wisconsin+WI'],
        "kolar": ["ClayBusters+TrapShooting+gun+guns+shotgun"],
    },
    "search_groups": {
        "milwaukee": ['WEEnergies', 'we energies', 'WE Energies', 'WE Energy', 'we energy', 'we energ*', 'WE Energ*'],
        "kolar": ['k80', 'K-80', 'K80', 'R9', 'Kolar', 'kolar', 'klar', 'klr'],
    }
}


milwaukee_subreddit = smootCityReddit.subreddit(t_configs["subreddit_groups"]["milwaukee"])
kolar_subreddit = smootCityReddit.subreddit(t_configs["subreddit_groups"]["kolar"])



for comment in kolar_subreddit.comments(limit=None):
    for itemtofind in t_configs["search_groups"]["kolar"]:
        if itemtofind in comment.body:
            print(f"comment: {comment.body}\n\n\n\n\n")     #   print pretty


