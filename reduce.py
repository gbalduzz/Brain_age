from modules import file_IO, preprocessing
import numpy as np
import h5py

f = h5py.File("preprocessed/reduced.hdf5", "w")
# Size of the data block to be averaged.
block_dims = np.array([4,4,4])

for name in ["train", "test"]:
    data1 = preprocessing.remove_zero_columns(
        file_IO.load_directory("set_" + name + "/grey_matter/", block_dims))
    data2 = preprocessing.remove_zero_columns(
        file_IO.load_directory("set_" + name + "/white_matter/", block_dims))
    data3 = preprocessing.remove_zero_columns(
        file_IO.load_directory("set_" + name + "/spinal_fluid/", block_dims))

    f.create_dataset(name, data=np.concatenate(data1, data2, data3, axis=1))
    print("saved: ", name)

f.close()
