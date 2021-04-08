from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import joblib


class Doc2vecInputHelper:
    """create iterable generator for Doc2Vec Input

    Args:
        subreddit (praw.subreddit): subreddit instance to parse through

    Examples:
        helper = Doc2VecModelHelper(model_kwargs=doc2vec_kwargs, fname="tests/tmp_outputs/d2v_model.joblib")
        d2v_model = helper.init_model()
        d2v_model.build_vocab(corpus_iterable=Doc2vecInputHelper(energy_subreddit))
        d2v_model.train(corpus_iterable=Doc2vecInputHelper(energy_subreddit), total_examples=d2v_model.corpus_count,
                        epochs=d2v_model.epochs)  # same ol' issue D2V generator input
    """

    def __init__(self, subreddit):
        self.subreddit = subreddit

    def __iter__(self):
        yield from (
            TaggedDocument(words=rdt_cmt.body.split(), tags=[rdt_cmt.subreddit_id, rdt_cmt.parent_id, rdt_cmt.id])
            for rdt_cmt in self.subreddit.comments()
        )


class Doc2VecModelHelper:
    """makes all of the setup easier when paired with InputHelper generator

    Args:
        model_kwargs (dict): dictionary of configurations for Doc2Vec model
        fname (str or Path): filename / path including final name for model

    Example:
        helper = Doc2VecModelHelper(model_kwargs=doc2vec_kwargs, fname="tests/tmp_outputs/d2v_model.joblib")
        d2v_model = helper.init_model()
        d2v_model.build_vocab(corpus_iterable=Doc2vecInputHelper(energy_subreddit))
        d2v_model.train(corpus_iterable=Doc2vecInputHelper(energy_subreddit), total_examples=d2v_model.corpus_count,
                        epochs=d2v_model.epochs)  # same ol' issue D2V generator input
    """

    def __init__(self, model_kwargs, fname):
        self.model_kwargs = model_kwargs
        self.fname = fname

    def init_model(self):
        return Doc2Vec(**self.model_kwargs)

    def save_model(self, to_save, compress):
        tmp_f = (self.fname + '.z' if compress else self.fname)
        joblib.dump(to_save, tmp_f)  # save compressed

        print(f"Saved {tmp_f}")
