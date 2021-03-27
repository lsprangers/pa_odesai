# from nlp_brew.connect_online import reddit

import os
import praw
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from dotenv import load_dotenv
import logging
import joblib

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


class Doc2vecInputHelper:

    def __init__(self, subreddit):
        self.subreddit = subreddit

    def __iter__(self):
        yield from (
            TaggedDocument(words=rdt_cmt.body.split(), tags=[rdt_cmt.subreddit_id, rdt_cmt.parent_id, rdt_cmt.id])
            for rdt_cmt in self.subreddit.comments()
        )


class Doc2VecModelHelper:

    def __init__(self, model_kwargs, fname):
        self.model_kwargs = model_kwargs
        self.fname = fname

    def init_model(self):
        return Doc2Vec(**self.model_kwargs)


rdt = praw.Reddit(**rdt_kwargs)

energy_list = 'RenewableEnergy+hardenergy+energypolitics+oilandgasworkers+Oil+wisconsin+milwaukee'
energy_subreddit = rdt.subreddit(energy_list)

helper = Doc2VecModelHelper(model_kwargs=doc2vec_kwargs, fname="tests/tmp_outputs/d2v_model.joblib")

d2v_model = helper.init_model()
d2v_model.build_vocab(corpus_iterable=Doc2vecInputHelper(energy_subreddit))
d2v_model.train(corpus_iterable=Doc2vecInputHelper(energy_subreddit), total_examples=d2v_model.corpus_count,
                epochs=d2v_model.epochs)  # same ol' issue D2V generator input

print('Saving Now')
joblib.dump(d2v_model, helper.fname + '.z')  # save compressed

print(f"Saved {helper.fname}")

praw_attrs = [x for x in dir(praw) if '__' not in x]  # ignore private vars
print('praw attributes: \n')
for att in praw_attrs:
    print(str(att))

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
