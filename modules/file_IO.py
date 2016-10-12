NUM_THREADS = 4

import nibabel
import numpy as np
import os
from multiprocessing.pool import ThreadPool

def load_directory(dirname):
    """
    :param dirname: relative dir path
    :return: np. array with n_files, n_features dimensions
    """
    path=os.getcwd()+"/"+dirname
    filenames = [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
    n = len(filenames)

    type = filenames[0].split('_')[0]
    assert(type == "train" or type=="test")
    sample_shape = nibabel.load(path+filenames[0]).shape
    four_d = (len(sample_shape) == 4)
    n_features = np.prod(sample_shape[0]*sample_shape[1]*sample_shape[2])
    x = np.zeros([n,n_features])

    pool = ThreadPool(NUM_THREADS)
    def load_file(i): # work item
        filename = path+"/"+type+"_"+str(i+1)+".nii"
        data=nibabel.load(filename).get_data()
        if four_d: data = data[:,:,:,0]
        x[i]= np.ndarray.flatten(data)

    pool.map(load_file, range(n))
    return x


def sum_data(filename):
    file = nibabel.load(filename)
    return sum(np.ndarray.flatten(file.get_data()))

def sum_partial_data(filename, boundaries):
    file = nibabel.load(filename)
    data = file.get_data()[boundaries[0][0]:boundaries[0][1],boundaries[1][0]:boundaries[1][1], boundaries[2][0]:boundaries[2][1]]
    return sum(np.ndarray.flatten(data))
