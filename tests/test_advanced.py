import sys
sys.path.extend(['.', '../', '../../'])

from nlp_brew.lil_models.bigbrain import TestBert

bert_args = {
    'directions': 'test',
}

me_BERT = TestBert(model_configs=bert_args)

me_BERT.look_around()

print('Done')

# from dotenv import load_dotenv
# import logging
# import os
# from nlp_brew.connect_online import reddit
#
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# load_dotenv(verbose=True)
# reddit_args = {
#     'client_id': os.getenv("REDDIT_CLIENT_ID"),
#     'client_secret': os.getenv("REDDIT_CLIENT_SECRET"),
#     'username': os.getenv("REDDIT_USERNAME"),
#     'password': os.getenv("REDDIT_PASSWORD"),
#     'user_agent': "Checking:It:Out by (/smoot)",
# }
# energy_subreddit = reddit.SmootPraw(**reddit_args).get_common_subreddit('energy')
