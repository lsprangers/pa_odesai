import sys
sys.path.extend(['.', '../', '../../', './nlp_brew/'])

import os
import logging

from dotenv import load_dotenv
from nlp_brew.connect_online import reddit as ls_reddit
from nlp_brew.lil_models.tokenizer_from_scratch import TokenizerInputHelper

from tokenizers import ByteLevelBPETokenizer
from tokenizers.processors import BertProcessing


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
load_dotenv(verbose=True)

rdt_kwargs = {
    "client_id": os.getenv("REDDIT_CLIENT_ID"),
    "client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
    "username": os.getenv("REDDIT_USERNAME"),
    "password": os.getenv("REDDIT_PASSWORD"),
    "user_agent": "Checking:It:Out by (/smoot)",
}
output_fname = "tests/tmp_outputs/"
model_output_name = "smoot_tokenizer"
bool_train_from_scratch = True

if bool_train_from_scratch:

    tokenizer_input_generator = TokenizerInputHelper(
        subreddit=ls_reddit.SmootPraw(rdt_kwargs).get_common_subreddit('energy'))

    me_tokenizer = ByteLevelBPETokenizer()

    me_tokenizer.train_from_iterator(
        iterator=tokenizer_input_generator,
        vocab_size=50,
        min_frequency=2,
        special_tokens=[
            "<s>",
            "<pad>",
            "</s>",
            "<unk>",
            "<mask>",
        ]
    )

    me_tokenizer.save_model(output_fname, model_output_name)


else:   # If you've already built and saved a model then this skips re-training

    me_tokenizer = ByteLevelBPETokenizer(
        f"{output_fname}{model_output_name}-vocab.json",
        f"{output_fname}{model_output_name}-merges.txt",
    )


me_tokenizer._tokenizer.post_processor = BertProcessing(
    ("</s>", me_tokenizer.token_to_id("</s>")),
    ("<s>", me_tokenizer.token_to_id("<s>")),
)
me_tokenizer.enable_truncation(max_length=512)

example_to_encode = "A reddit comment will jdhfbgw hehehehe RAWR XD :)))"
print(f"\n\nENCODING: \n\t{example_to_encode}...\n...\n...")

example_encoded = me_tokenizer.encode(example_to_encode)
print(example_encoded)
print(example_encoded.tokens)

print(f"\n...\n...\nEncoder Built - Script Complete\n...\n...\n...")
