# theAteam.
*  Giovanni Balduzzi
*  Samarth Shuckla
*  Olga Klimashevska
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

##Description.

The prediction is first made by excracting the spinal fluid, white and grey matter with the _fast_ library. Each component is averaged over 2x2x2 blocks so that it can fit into memory (approx 10 GB required) and the resulting averaged voxels used as features. Voxels that are 0 across all training sets are removed.
 As we noted there is a strong dependence of the age from the size of the central ventriculum, me added a feature made by the ratio of the fluid in the central zone of the brain over the total size of white and grey matter. The log of this quantity is also used (see _ageVsCentralFluidRatio.pdf_).This features are then used to train  an elastic band model, with parameters chosen with a 5-fold CV.
