
from transformers import (
    pipeline,
    DistilBertForTokenClassification,
    DistilBertTokenizer,
    TapasForQuestionAnswering
)
from connect_to_db import KaggleBaseballDatabaseConnector


distilbert_model = DistilBertForTokenClassification.from_pretrained("distilbert-base-cased")
distilbert_tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-cased")
ner_pipe = pipeline('ner', model=distilbert_model, tokenizer=distilbert_tokenizer)

tapas_model = TapasForQuestionAnswering.from_pretrained("distilbert-base-cased")
tq_pipe = pipeline(task='table-question-answering', model=tapas_model, tokenizer=distilbert_tokenizer)

kaggler = KaggleBaseballDatabaseConnector()
kaggler.print_all_tables()

print('File done')