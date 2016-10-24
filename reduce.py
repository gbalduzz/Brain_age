from modules import file_IO, preprocessing
import numpy as np
import h5py


f = h5py.File("preprocessed/reduced.hdf5", "w")

def load_component(comp_name):
    """
    return: 1) array of shape n_train+n_test, comp_size
            2) n_train
    """
    data = file_IO.load_directory("set_train/"+comp_name+"/")
    n_train = data.shape[0]
    data = np.concatenate((data,
                           file_IO.load_directory("set_test/" + comp_name + "/")
                          ), axis = 0)
    return preprocessing.remove_zero_columns(data, n_train), n_train

data1, n_train = load_component("grey_matter")
print("loaded grey with size", data1.shape)
data2, _ = load_component("white_matter")
print("loaded white with size", data2.shape)
data3, _ = load_component("spinal_fluid")
print("loaded fluid with size", data3.shape)

f.create_dataset("train_data", data=np.concatenate((data1, data2, data3), axis=1)[:n_train, :])
f.create_dataset("test_data",  data=np.concatenate((data1, data2, data3), axis=1)[n_train:, :])
print("n train dataset: ", n_train)

f.close()
