# Age determination from brain  MRI scans.
##Prerequisites

* fsl library, available [here](http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/). Used for extracting brain components.
* python 2.7 modules: numpy, skilearn, nibabel, h5py.
* the data set stored in `set_train/train_<id>.nii` and  `set_test/test_<id>.nii`

## Preprocess
run the following scripts to extract the brain components and reduce their size by averaging over blocks (size of blocks defined in reduce.py).
```
bash extrac_components.bash # runs the fsl software
python2.7 reduce.py
python2.7 compute_ratio.py # optional: ratio already precomputed in folder preprocessed/
```
## Make the predictions
Run 
```
python2.7 main.py
```
The predicted ages will be stored in `predict.csv`. You can run 
```format.py```
to format the prediction into the kraggle submission format.
