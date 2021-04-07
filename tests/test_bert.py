import sys
sys.path.extend(['.', '../', '../../', './nlp_brew/'])

import os
import logging

from dotenv import load_dotenv
from nlp_brew.connect_online import reddit as ls_reddit
from nlp_brew.lil_models.bertbrain import BertInputHelper, BertModel


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

meHelper = BertInputHelper(subreddit=subr)

bert = BertModel(
    corpus=meHelper.get_comments_for_bert(),
)

bert_features = bert.stack_final_layer()
