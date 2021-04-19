import re
import numpy as np
import unicodedata
import torch
import transformers

import nltk

nltk.download('stopwords')
STOPWORDS = nltk.corpus.stopwords.words('english')


class TextPreProcessor:
    def __init__(self, sentence):
        self.sentence = sentence

    @staticmethod
    def quick_unicode2ascii(sent_strip):
        return "".join(
            y
            for y in unicodedata.normalize("NFD", sent_strip)
            if unicodedata.category(y) != "Mn"
        )

    @staticmethod
    def quick_clean_stopwords_and_shortwords(w):
        words = w.split()
        cleaned = [
            wr for wr in words if (wr not in STOPWORDS) and len(wr) > 2
        ]
        return " ".join(cleaned)

    def process_sentence(self):
        w = self.sentence
        w = self.quick_unicode2ascii(w.lower().strip())
        w = re.sub(r"[?.!,:;]", r" ", w)
        w = re.sub(r'[" "]+', " ", w)
        w = re.sub("[^a-zA-z>.!,:;]+", " ", w)
        w = self.quick_clean_stopwords_and_shortwords(w)
        w = re.sub(r"@\w+", "", w)
        return w


class BertInputHelper:
    def __init__(self, subreddit):
        self.subreddit = subreddit

    def get_comments_for_bert(self):
        yield from (
            TextPreProcessor(rdt_cmt.body).process_sentence()
            for rdt_cmt in self.subreddit.comments()
        )


class BertModel:

    def __init__(self, corpus):
        self.b_model = transformers.DistilBertModel.from_pretrained("distilbert-base-cased")
        self.b_tokenizer = transformers.DistilBertTokenizer.from_pretrained("distilbert-base-cased")
        self.corpus = corpus

    def tokenize_tensors(self):
        return self.b_tokenizer(
            [x for x in self.corpus],
            add_special_tokens=True,
            max_length=70,
            truncation=True,
            padding='max_length',
            return_attention_mask=True,
            verbose=True,
            return_tensors="pt"
        )

    def stack_final_layer(self):
        with torch.no_grad():
            last_hidden_states = self.b_model(**self.tokenize_tensors())

        return last_hidden_states[0][:, 0, :].numpy()
