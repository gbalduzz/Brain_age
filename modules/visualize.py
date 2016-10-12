import nibabel
import numpy as np
import matplotlib.pyplot as plt

# Horribly copy pasted visualization functions
def visualize_z_slice(filename, z):
    file = nibabel.load(filename)
    if len(file.shape) == 4 :
        data = file.get_data()[:,:,z,0]
    else :
        data = file.get_data()[:, :, z]
    plt.imshow(data.T, cmap="gray", origin="lower")

def visualize_x_slice(filename, x):
    file = nibabel.load(filename)
    if len(file.shape) == 4:
        data = file.get_data()[x, :, :, 0]
    else:
        data = file.get_data()[x, :, :]
    plt.imshow(data.T, cmap="gray", origin="lower")

def visualize_partial_z_slice(filename,  lx, ly =100):
    file = nibabel.load(filename)
    v0 = np.array(file.shape)/2;
    data = file.get_data()[v0[0]-lx/2:v0[0]+lx/2, v0[1]-ly/2:v0[1]+ly/2, v0[2]]
    plt.imshow(data.T, cmap="gray", origin="lower")

def visualize_partial_x_slice(filename,  ly, lz):
    file = nibabel.load(filename)
    v0 = np.array(file.shape)/2;
    data = file.get_data()[v0[0], v0[1]-ly/2:v0[1]+ly/2, v0[2]-lz/2:v0[2]+lz/2]
    plt.imshow(data.T, cmap="gray", origin="lower")
