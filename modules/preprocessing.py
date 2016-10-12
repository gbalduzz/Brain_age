import numpy as np

def remove_zero_columns(x,tollerance=0):
    """
    :param x: array to reduce, assumed positive
    :param tollerance: maximum abs value that is considered zero
    :return: np.array with removed columns
    """
    max_values = np.amax(x, axis=0)
    mask = np.ones(max_values.shape)*tollerance
    keep_indices = np.greater(max_values,mask)
    return x[:, keep_indices]

max
