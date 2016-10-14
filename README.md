# Age determination from brain scans.
## Prepare the data
Unzip the data set in this folder, with the training files named `set_train/train_<n>.nii` and the validation files `set_test/test_<n>.nii`
## Preprocess
run the following scripts to extract the brain compomnents and reduce their size
```
bash extrac_components.bash
python2.7 reduce.py
python2.7 compute_ratio.py # optional: ratio already precomputed in folder preprocessed/
```
## Make the predictions
Run 
```
python2.7 main.py
```
The predicted ages will be stored in `predict.csv`. You might want to play around with the parameters of the Elastic Net model.
