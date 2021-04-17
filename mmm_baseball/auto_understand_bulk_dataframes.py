
# *Not Recommended: pip install tensorflow --upgrade
#   ...can degrade numpy and cause SIGILL error

# conda update -f -c conda-forge tensorflow
import transformers # , DistilBertModel, DistilBertTokenizer
from connect_to_db import KaggleBaseballDatabaseConnector


# model = DistilBertModel.from_pretrained("distilbert-base-cased")
# tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-cased")
# ner_pipe = pipelines('ner', model=model, tokenizer=tokenizer)

# needs pytorch_scatter, and pytorch 1.4
tq_pipe = transformers.pipeline('table-question-answering')

kaggler = KaggleBaseballDatabaseConnector()

kaggler.print_all_tables()

print('File done')