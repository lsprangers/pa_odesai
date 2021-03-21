import sys
from importlib import import_module

# TODO: @Luke_Sprangers --> Create DRY function to import stuff -- confused on how to make this simple.
libs_pure = ['gensim.models.Doc2Vec', 'numpy', 'pandas']

for libname in libs_pure:
    try:
        lib = import_module(libname)
    except ImportError as e:
        print(f"{sys.exc_info()}")
    else:
        globals()[libname] = lib


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
