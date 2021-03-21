import sys
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text
import matplotlib.pyplot as plt
import numpy
import shutil
import nltk
import official.nlp.optimization

class FrostyTheSnowman(dict):
    """try to do something worthwhile

    Args:
        model_configs (dict): dictionary of configurations for BERT model

    Params:
        model_configs          (dict): dictionary of configurations for BERT model
        batch_size              (int): size of each batch
        seed                    (int): seed for reproducibility
        standford_testing_url   (str): url to stanford testing datasets

    Example:
        my_word_model = FrostyTheSnowman(mdl_configs)
        my_word_model.look_around()
    """

    tf.get_logger().setLevel('ERROR')

    def __init__(self, model_configs):
        self.model_configs = model_configs
        self.AUTOTUNE = tf.data.AUTOTUNE
        self.batch_size = 32
        self.seed = 42

        if 'test' in self.model_configs['directions']:
            self.standford_testing_url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
            self.dataset = tf.keras.utils.get_file('aclImdb_v1.tar.gz', self.standford_testing_url,
                                                   untar=True, cache_dir='',
                                                   cache_subdir='')

            self.dataset_dir = os.path.join(os.path.dirname(self.dataset), 'aclImdb')

            self.train_dir = os.path.join(self.dataset_dir, 'train')

            # remove unused folders to make it easier to load the data
            self.remove_dir = os.path.join(self.train_dir, 'unsup')
            shutil.rmtree(self.remove_dir)

        if "NO SETUP" not in self.model_configs['directions']:

            self.raw_train_ds = tf.keras.preprocessing.text_dataset_from_directory(
                'aclImdb/train',
                batch_size=self.batch_size,
                validation_split=0.2,
                subset='training',
                seed=self.seed)

            self.class_names = self.raw_train_ds.class_names
            self.train_ds = self.raw_train_ds.cache().prefetch(buffer_size=self.AUTOTUNE)

            self.val_ds = tf.keras.preprocessing.text_dataset_from_directory(
                'aclImdb/train',
                batch_size=self.batch_size,
                validation_split=0.2,
                subset='validation',
                seed=self.seed)

            self.val_ds = self.val_ds.cache().prefetch(buffer_size=self.AUTOTUNE)

            self.test_ds = tf.keras.preprocessing.text_dataset_from_directory(
                'aclImdb/test',
                batch_size=self.batch_size)

            self.test_ds = self.test_ds.cache().prefetch(buffer_size=self.AUTOTUNE)

        else:
            print("not setting up")

    def look_around(self):
        """take a look around and make sure it all works
        """
        for text_batch, label_batch in self.train_ds.take(1):
            for i in range(3):
                print(f'Review: {text_batch.numpy()[i]}')
                label = label_batch.numpy()[i]
                print(f'Label : {label} ({self.class_names[label]})')


# from filler_up.fill_it import GetTheBag
#
# lib_dict = {
#     'shorthand': [
#         ('tensorflow', 'tf'),
#         ('tensorflow_hub', 'hub'),
#         ('tensorflow_text', 'text'),
#         ('matplotlib.pyplot', 'plt'),
#     ],
#     'pure': ['numpy', 'shutil', 'nltk', 'official.nlp.optimization']
# }
# my_filler = GetTheBag(lib_dict)
# did_it_work = my_filler.go_get_it()
