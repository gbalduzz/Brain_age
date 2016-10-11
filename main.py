from modules.file_IO import sum_partial_data, sum_data
import matplotlib.pyplot as plt
import numpy as np
"""
 Read N_files from the training folder and output a plot of ventricular fluid/brain size vs age.
"""
### inputs ####
names = ["train", "test"]
N_files = [278, 138] # too lazy to automate this...
cached_sums=0; # read sums from file (compute them from scratch)
boundaries = [ # box where the central ventricul is supposed to be
    [52,121],
    [62,155],
    [76,102]
]
################

count =0
for name in names:
    N = N_files[count]
    x = np.zeros([N, 3])
    y = np.loadtxt("targets.csv")[0:N]

    if not cached_sums:
        for i in range(N):
            x[i,0] = sum_partial_data("set_"+name+"/spinal_fluid/"+name+"_"+str(i+1)+".nii", boundaries)
            x[i,1] = sum_data("set_"+name+"/grey_matter/"+name+"_"+str(i+1)+".nii")
            x[i,2] = sum_data("set_"+name+"/white_matter/"+name+"_"+str(i+1)+".nii")
            print("done: ", i+1)
        np.savetxt("preprocessed/partial_sums_"+name+"ing.csv",x)
    else:
        x = np.loadtxt("preprocessed/partial_sums_"+name+"ing.csv")

    # Play around to obtain interesting quantities:
    ratio = x[:,0]/(x[:,1]+x[:,2]) # central fluid / (white+grey)
    np.savetxt("ratio_"+name+"ing.csv", ratio)

    if name == "train": # plot
        plt.scatter(y,ratio)
        plt.title("central fluid - brain ratio")
        plt.xlabel("age")
        plt.savefig("central_fluid_ratio.pdf")

    count += 1
plt.show()
