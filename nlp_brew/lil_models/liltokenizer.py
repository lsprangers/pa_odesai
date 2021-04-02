from tokenizers import Tokenizer, trainers, models
from tokenizers import processors


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
            rdt_cmt.body
            for rdt_cmt in self.subreddit.comments()
        )


class TokenizerHelper:
    """create Tokenizer - huggingface.io examples/pkgs

    Args:
         inputter (generator): subreddit instance to parse through

    Examples:
        helper = Doc2VecModelHelper(model_kwargs=doc2vec_kwargs, fname="tests/tmp_outputs/d2v_model.joblib")
        d2v_model = helper.init_model()
        d2v_model.build_vocab(corpus_iterable=Doc2vecInputHelper(energy_subreddit))
        d2v_model.train(corpus_iterable=Doc2vecInputHelper(energy_subreddit), total_examples=d2v_model.corpus_count,
                        epochs=d2v_model.epochs)  # same ol' issue D2V generator input
    """

    def __init__(self, output_fname, model_output_name, inputter):
        self.output_fname = output_fname
        self.model_output_name = model_output_name
        self.full_model_path = f"{self.output_fname}{self.model_output_name}.tokenizer.json"
        self.inputter = inputter
        self.tokenizer = Tokenizer(models.BPE())

    def build_bert_tokenizer(self):
        inp_gen = self.inputter

        trainer = trainers.BpeTrainer(
            vocab_size=20000,
            min_frequency=2,
            special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"]
        )

        self.tokenizer.train_from_iterator(
            iterator=inp_gen, trainer=trainer)

        self.tokenizer.post_processor = processors.TemplateProcessing(
            single="[CLS] $A [SEP]",
            pair="[CLS] $A [SEP] $B:1 [SEP]:1",
            special_tokens=[
                ("[CLS]", 1),
                ("[SEP]", 2),
            ],
        )

    def import_local_tokenizer(self):
        self.tokenizer = Tokenizer.from_file(self.full_model_path)

    def save_tokenizer(self):
        self.tokenizer.save(self.full_model_path, pretty=True)
