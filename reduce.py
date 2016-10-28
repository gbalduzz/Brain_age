from modules import file_IO, preprocessing
import numpy as np
import h5py

# number of feature per measurments.
n_feat = 200

f = h5py.File("preprocessed/reduced.hdf5", "w")

def load_component(comp_name, n_feat=100):
    """
    return: 1) array of shape n_train+n_test, comp_size
            2) n_train
    """
    train = file_IO.load_directory("set_train/"+comp_name+"/")
    test = file_IO.load_directory("set_test/" + comp_name + "/")
    return preprocessing.max_variabilty(train, test, n_feat)

train1, test1 = load_component("grey_matter")
print("loaded grey with size", train1.shape)
train2, test2 = load_component("white_matter")
print("loaded white with size", train2.shape)
train3, test3 = load_component("spinal_fluid")
print("loaded fluid with size", train3.shape)

train = preprocessing.max_variabilty(np.concatenate((train1, train2, train3), axis=1))
test = preprocessing.max_variabilty(np.concatenate((test1, test2, test3), axis=1))
train, test = preprocessing.max_variabilty(train, test, n_feat=n_feat)

f.create_dataset("train_data", train)
f.create_dataset("test_data",  test)

f.close()
