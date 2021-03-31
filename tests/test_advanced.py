import sys
sys.path.extend(['.', '../', '../../', './nlp_brew/'])

from nlp_brew.lil_models import brain_from_scratch
import os
import logging
from tokenizers import ByteLevelBPETokenizer
from dotenv import load_dotenv
from nlp_brew.connect_online import reddit as ls_reddit
from nlp_brew.lil_models.brain_from_scratch import TokenizerInputHelper


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
load_dotenv(verbose=True)

rdt_kwargs = {
    "client_id": os.getenv("REDDIT_CLIENT_ID"),
    "client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
    "username": os.getenv("REDDIT_USERNAME"),
    "password": os.getenv("REDDIT_PASSWORD"),
    "user_agent": "Checking:It:Out by (/smoot)",
}

tokenizer_input_generator = TokenizerInputHelper(
    subreddit=ls_reddit.SmootPraw(rdt_kwargs).get_common_subreddit('energy'))

my_tokenizer = ByteLevelBPETokenizer()

my_tokenizer.train_from_iterator(
            iterator=tokenizer_input_generator, vocab_size=50, min_frequency=2)

my_tokenizer.save_model("tests/tmp_outputs/", "smoot_tokenizer")
