from gensim.models import Doc2Vec


class simple_thinker():
    """try to do something worthwhile

    Examples:
        >>> from nlp_brew.brainz import lilbrain
        >>> my_word_model = lilbrain.simple_thinker().get_gensim_docvec_model()
    """

    def __init__(self, model_configs):
        self.model_configs = model_configs

    def get_gensim_docvec_model(self):
        return Doc2Vec(**self.model_configs["doc2vec"])
