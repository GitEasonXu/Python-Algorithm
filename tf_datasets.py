from numpy.lib.shape_base import _replace_zero_by_x_arrays
import tensorflow as tf
import numpy as np
from collections import Iterable


features_batch = np.ones((100, 5))
labels_batch = np.zeros((100, 5))
data = (features_batch, labels_batch)

datasets = tf.data.Dataset.from_tensor_slices(data).batch(2)


# print("TF Dataset is iterable:", isinstance(datasets,Iterable))
# for x_data, y_data in datasets:
#     print(x_data.shape)
#     print(type(x_data))


class closing(object):
    def __enter__(self):
        print("1------------------------")
        return None
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("1======================")
class closing2(object):
    def __enter__(self):
        print("2------------------------")
        return None
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("2======================")

with closing(), closing2():
    pass
