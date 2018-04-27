import numpy as np
import pandas as pd
from tensorflow.contrib.learn.python.learn.datasets import base
from sklearn.utils import shuffle


class DataSet(object):

    def __init__(self,
                 face,
                 labels,
                 one_hot=False):

        if one_hot==True:
            num_labels = len(np.unique(labels))
            labels = np.eye(num_labels)[labels]

        self._num_examples = len(face)
        self._faces = face
        self._labels = labels
        self._epochs_completed = 0
        self._index_in_epoch = 0
        self._all_x = None
        self._all_y = None

    @property
    def faces(self):
        return self._faces

    @property
    def labels(self):
        return self._labels

    @property
    def num_examples(self):
        return self._num_examples

    @property
    def epochs_completed(self):
        return self._epochs_completed

    def next_batch(self, batch_size):

        start = self._index_in_epoch
        self._index_in_epoch += batch_size
        if self._index_in_epoch > self._num_examples:
            # Finished epoch
            self._epochs_completed += 1
            # Shuffle the data
            perm = np.arange(self._num_examples)
            np.random.shuffle(perm)
            self._faces = self._faces[perm]
            self._labels = self._labels[perm]
            # Start next epoch
            start = 0
            self._index_in_epoch = batch_size
            assert batch_size <= self._num_examples
        end = self._index_in_epoch
        return self._faces[start:end], self._labels[start:end]



def randomize(dataset, labels):
  permutation = np.random.permutation(labels.shape[0])
  shuffled_dataset = dataset[permutation,:,:]
  shuffled_labels = labels[permutation]
  return shuffled_dataset, shuffled_labels


def get_face_data(file_url,output_column_index=0,test_size=0.30, random_state=42):

    if file_url is not None:
        dataframe=pd.read_csv(file_url) # columns['emotion', 'pixels', 'Usage']

        train = dataframe[dataframe['Usage'] == 'Training']
        test = dataframe[dataframe['Usage'] == 'PublicTest']
        train_pixels_data = train['pixels']
        test_pixels_data = test['pixels']
        train_data = []
        test_data = []
        for i, row in train_pixels_data.iteritems():
            pixel_slice = list(map(int, row.split(' ')))
            train_data.append(pixel_slice)

        for i, row in test_pixels_data.iteritems():
            pixel_slice = list(map(int, row.split(' ')))
            test_data.append(pixel_slice)

        train_labels = train['emotion']
        test_labels = test['emotion']



        train_labels = np.squeeze(np.asarray(train_labels))
        test_labels = np.squeeze(np.asarray(test_labels))

        train_data = np.asarray(train_data)
        test_data = np.asarray(test_data)
        train_data = train_data/255.0
        test_data = test_data/255.0

        train_data, train_labels=shuffle(train_data,train_labels,random_state=42)
        test_data, test_labels=shuffle(test_data,test_labels,random_state=42)


        return [train_data, test_data, train_labels, test_labels]




def get_face_data_as_object(file_url,output_column_index,test_size=0.30, random_state=42):
    train_data, test_data, train_labels, test_labels = get_face_data(file_url,output_column_index,test_size, random_state)

    train = DataSet(train_data, train_labels, one_hot=True)
    test = DataSet(test_data, test_labels, one_hot=True)
    return base.Datasets(train=train, validation=None, test=test)
