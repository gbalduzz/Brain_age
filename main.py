import nibabel
import matplotlib.pyplot as plt

file = nibabel.load("set_test/test_1.nii")
data = file.get_data()[:,:,:,0]
print(data.shape)

#plt.imshow(data[:,:,100].T,cmap="gray", origin="lower")
#plt.show()
