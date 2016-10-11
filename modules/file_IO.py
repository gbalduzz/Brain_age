import nibabel
import numpy as np
import matplotlib.pyplot as plt

def sum_data(filename):
    file = nibabel.load(filename)
    return sum(np.ndarray.flatten(file.get_data()))

def visualize_slice(filename, z):
    file = nibabel.load(filename)
    if len(file.shape) == 4 :
        data = file.get_data()[:,:,z,0]
    else :
        data = file.get_data()[:, :, z]
    plt.imshow(data.T, cmap="gray", origin="lower")
