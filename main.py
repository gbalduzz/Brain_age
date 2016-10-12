from modules import file_IO, preprocessing
import numpy as np

grey = preprocessing.remove_zero_columns(file_IO.load_directory("set_train/grey_matter/"))
print(grey.shape)

