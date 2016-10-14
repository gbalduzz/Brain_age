from modules import file_IO, preprocessing
import numpy as np
from sklearn import preprocessing, linear_model
import h5py
import time

file = h5py.File("preprocessed/reduced.hdf5", "r")

#read the data
train = np.array(file.get("train_data"))
test  = np.array(file.get("test_data"))

y = np.loadtxt("targets.csv") # targets for train set
file.close()

#add feature from the ratio
def append_ratio(set, filename):
    ratio = np.loadtxt(filename).T
    return np.column_stack((set, ratio, ratio*ratio))

train = append_ratio(train, "preprocessed/ratio_training.csv")
test = append_ratio(test, "preprocessed/ratio_test.csv")

# Scaling
scaler = preprocessing.StandardScaler().fit(train)
train = scaler.transform(train)
test = scaler.transform(test)

# Train the Model
start = time.clock()
print("start training")
regr = linear_model.ElasticNetCV(l1_ratio = [.5, .75, .95], normalize=True, cv = 5, n_jobs=-1)
regr.fit(train,y)
finish = time.clock()
print("training time: ", finish-start)

# Make Predictions and save
prediction = regr.predict(test)
np.save("prediction.csv", prediction)

