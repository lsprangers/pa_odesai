import sys
from filler_up import fill_it

lib_dict = {
    'shorthand': None,
    'pure': ['gensim.models.Doc2Vec', 'numpy', 'nltk', 'pandas']
}

my_filler = fill_it.GetTheBag(lib_dict)
did_it_work = my_filler.go_get_it()

if did_it_work:
    print("it worked!")
else:
    print("try again")


class Simpleton(dict):
    """try to do something worthwhile - easier

    Args:
        model_configs (dict): dictionary of configurations for Doc2Vec model

    Examples:
        my_word_model = Simpleton(mdl_configs).get_gensim_docvec_model()
    """

    def __init__(self, model_configs):
        self.model_configs = model_configs

    def get_gensim_docvec_model(self):
        return Doc2Vec(**self.model_configs["doc2vec"])
