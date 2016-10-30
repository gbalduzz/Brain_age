#!/usr/bin/bash
echo "extracting brain components. This might take a while..."
bash extract_components.bash
python2.7 compute_ratio.py
echo "Averaging voxels..."
python2.7 reduce.py
echo "Training model..."
python2.7 main.py
python2.7 format.py
echo "Prediction stored in final_prediction.csv"
