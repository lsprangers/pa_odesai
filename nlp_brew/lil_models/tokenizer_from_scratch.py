
def bert_pad(str_to_fmt):
    return ["<s>"] + str_to_fmt.split() + ["</s>"]


class TokenizerInputHelper:
    """create iterable generator for scratch Tokenizer input

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
            bert_pad(rdt_cmt.body)
            for rdt_cmt in self.subreddit.comments()
        )
