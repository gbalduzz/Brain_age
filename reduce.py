from modules import file_IO, preprocessing
import numpy as np
import h5py

f = h5py.File("preprocessed/reduced.hdf5", "w")

def reduce(out_name, dir):
    reduced = preprocessing.remove_zero_columns(file_IO.load_directory(dir))
    f.create_dataset(out_name, data=reduced)

    print("saved: ", out_name, "with size ",reduced.shape)



for name in ["train", "test"]:
    reduce(name+"_grey", "set_"+name+"/grey_matter/")
    reduce(name+"_white", "set_"+name+"/white_matter/")
    reduce(name+"_fluid", "set_"+name+"/spinal_fluid/")

f.close()
