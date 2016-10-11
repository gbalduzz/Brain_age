import modules.file_IO as IO
import matplotlib.pyplot as plt
####
set =2
z = 176/2
####

IO.visualize_slice("set_train/spinal_fluid/train_"+str(set)+".nii", z)
plt.show()
