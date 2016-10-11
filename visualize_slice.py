import modules.file_IO as IO
import matplotlib.pyplot as plt

# Play aroundd with this file to print 2D images of the .nii files
#### inputs
set =127
lx = 66
ly = 100
lz = 100
####

IO.visualize_z_slice("set_train/spinal_fluid/train_"+str(set)+".nii", 176/2)
#IO.visualize_partial_z_slice("set_train/spinal_fluid/train_"+str(set)+".nii", lx, ly)
#IO.visualize_x_slice("set_train/spinal_fluid/train_"+str(set)+".nii", 176/2)
plt.show()
