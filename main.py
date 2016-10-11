from modules.file_IO import sum_data
import matplotlib.pyplot as plt
import numpy as np

N_files = 278
cached_sums=1;


x = np.zeros([N_files, 3])
y = np.loadtxt("targets.csv")[0:N_files]

if not cached_sums:
    for i in range(N_files):
        try:
            x[i,0] = sum_data("set_train/spinal_fluid/train_"+str(i+1)+".nii")
            x[i,1] = sum_data("set_train/grey_matter/train_"+str(i+1)+".nii")
            x[i,2] = sum_data("set_train/white_matter/train_"+str(i+1)+".nii")
            print("done: ", i+1)
        except:
            x[i] = [0,0,0]
            print("failed: ", i+1)

    np.savetxt("sums.csv",x)
else:
    x = np.loadtxt("sums.csv")

plt.scatter(y,x[:,0]/(x[:,1]+x[:,2]))
plt.title("total fluid - brain ratio")
plt.xlabel("age")
#plt.savefig("total_fluid_ratio.pdf")
plt.show()

#clf = svm.SVC(gamma=0.001, C=100.)
#print("training...")
#clf.fit(x, y)

