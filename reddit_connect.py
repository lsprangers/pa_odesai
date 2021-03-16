import praw
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

reddit_obj = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    password=os.getenv("REDDIT_PASSWORD"),
    username=os.getenv("REDDIT_USERNAME"),
    user_agent="SmootCity:ResearchDept:Intern:V1 (by u/smoot_city)",
)


print(f"Is read only instance: {reddit.read_only}")
print(f"Me: {reddit.user.me()}")


subreddit = reddit.subreddit("milwaukee")

print(subreddit.display_name)


for submission in subreddit.hot(limit=10):
    print(submission.title)
    # Output: the submission's title
    print(submission.score)
    # Output: the submission's score
    print(submission.id)
    # Output: the submission's ID
    print(submission.url)
