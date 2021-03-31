import os
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text
import matplotlib.pyplot as plt
import numpy
import shutil
# import nltk
# import official.nlp.optimization


# bert_AUTOTUNE = tf.data.AUTOTUNE
bert_batch_size = 32
bert_seed = 42

standford_testing_url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
dataset = tf.keras.utils.get_file('aclImdb_v1.tar.gz', standford_testing_url,
                                  untar=True, cache_dir='',
                                  cache_subdir='')

dataset_dir = os.path.join(os.path.dirname(dataset), 'aclImdb')

train_dir = os.path.join(dataset_dir, 'train')

# remove unused folders to make it easier to load the data
remove_dir = os.path.join(train_dir, 'unsup')
shutil.rmtree(remove_dir)

raw_train_ds = tf.keras.preprocessing.text_dataset_from_directory(
    'aclImdb/train',
    bert_batch_size=bert_batch_size,
    validation_split=0.2,
    subset='training',
    bert_seed=bert_seed)

class_names = raw_train_ds.class_names
train_ds = raw_train_ds.cache().prefetch(buffer_size=bert_AUTOTUNE)

val_ds = tf.keras.preprocessing.text_dataset_from_directory(
    'aclImdb/train',
    bert_batch_size=bert_batch_size,
    validation_split=0.2,
    subset='validation',
    bert_seed=bert_seed)

val_ds = val_ds.cache().prefetch(buffer_size=bert_AUTOTUNE)

test_ds = tf.keras.preprocessing.text_dataset_from_directory(
    'aclImdb/test',
    bert_batch_size=bert_batch_size)

test_ds = test_ds.cache().prefetch(buffer_size=bert_AUTOTUNE)


for text_batch, label_batch in train_ds.take(1):
    for i in range(3):
        print(f'Review: {text_batch.numpy()[i]}')
        label = label_batch.numpy()[i]
        print(f'Label : {label} ({class_names[label]})')
