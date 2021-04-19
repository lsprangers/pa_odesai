import sys
sys.path.extend(['.', '../', '../../', './nlp_brew/'])

import os
import logging

from dotenv import load_dotenv
from nlp_brew.connect_online import reddit as ls_reddit
from nlp_brew.lil_models.liltokenizer import TokenizerInputHelper, TokenizerHelper


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
load_dotenv(verbose=True)

rdt_kwargs = {
    "client_id": os.getenv("REDDIT_CLIENT_ID"),
    "client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
    "username": os.getenv("REDDIT_USERNAME"),
    "password": os.getenv("REDDIT_PASSWORD"),
    "user_agent": "Checking:It:Out by (/smoot)",
}
output_f = "tests/tmp_outputs/"
model_name = "smoot_tokenizer2"
bool_tf_scratch = True
subr = ls_reddit.SmootPraw(rdt_kwargs).get_common_subreddit('energy')

meHelper = TokenizerInputHelper(subreddit=subr)

lilTokenizer = TokenizerHelper(
    output_fname=output_f,
    model_output_name=model_name,
    inputter=meHelper
)

lilTokenizer.build_bert_tokenizer()

lilTokenizer.save_tokenizer()
