from gensim.models import Doc2Vec


def think_by():
    """try to do something worthwhile

    Examples:
        >>> from brainz import lilbrain
        >>> my_word_model = lilbrain.think_by().looking_forward()
    """

    def __init__(self, model_configs):
        self.model_configs = model_configs

    def looking_forward(self):
        self.docvec_model = Doc2Vec(**self.model_configs["doc2vec"])
