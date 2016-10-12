from modules import file_IO, preprocessing
import numpy as np

def reduce(out_name, dir):
    reduced = preprocessing.remove_zero_columns(file_IO.load_directory(dir))
    np.savetxt("preprocessed/"+out_name, reduced)
    print("saved: ", out_name, "with size ",reduced.shape)

for name in ["train", "test"]:
    reduce(name+"_grey_reduced.csv", "set_"+name+"/grey_matter/")
    reduce(name+"_white_reduced.csv", "set_"+name+"/white_matter/")
    reduce(name+"_fluid_reduced.csv", "set_"+name+"/spinal_fluid/")
