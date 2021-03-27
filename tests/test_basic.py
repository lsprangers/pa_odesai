import os
import praw
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from dotenv import load_dotenv
import logging
import joblib
from nlp_brew.lil_models import lilbrain
from nlp_brew.connect_online import reddit

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
load_dotenv(verbose=True)

rdt_kwargs = {
    'client_id': os.getenv("REDDIT_CLIENT_ID"),
    'client_secret': os.getenv("REDDIT_CLIENT_SECRET"),
    'username': os.getenv("REDDIT_USERNAME"),
    'password': os.getenv("REDDIT_PASSWORD"),
    'user_agent': "Checking:It:Out by (/smoot)",
}
doc2vec_kwargs = {
    'vector_size': 150,
    'window': 10,
    'min_count': 2,
}

energy_subreddit = reddit.SmootPraw(**rdt_kwargs).get_common_subreddit('energy')

reddit.print_attributes(praw)
comment_attrs_to_print = [
    "parent_id",
    "subreddit_id",
    "link_id",
    "id",
    "author",
    "body",
    "body_html",
    "distinguished",
    "score",
]

for _, comment in zip(range(50), energy_subreddit.comments()):  # print first 50 comment (attributes) for show
    for t_att in comment_attrs_to_print:
        print(f"comment {t_att} \n {getattr(comment, t_att)} \n{'-' * 5}")

helper = lilbrain.Doc2VecModelHelper(model_kwargs=doc2vec_kwargs, fname="tests/tmp_outputs/d2v_model.joblib")

corpus = lilbrain.Doc2vecInputHelper(energy_subreddit)

d2v_model = helper.init_model()

d2v_model.build_vocab(
    corpus_iterable=corpus)

# same ol' issue D2V generator input
d2v_model.train(
    corpus_iterable=corpus, total_examples=d2v_model.corpus_count, epochs=d2v_model.epochs)

helper.save_model(d2v_model, compress=True)

print('Done')
