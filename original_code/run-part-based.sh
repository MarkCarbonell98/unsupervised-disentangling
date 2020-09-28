#! /usr/bin/env bash

N_KEYPOINTS=16
IMGS_PATH="experiments/baseline_deepfashion_256"

./run.sh -1
cp -v -r "$IMGS_PATH/transfer_plots" "$IMGS_PATH/transfer_plots_-1"

for IDX in $(seq 0 $((N_KEYPOINTS - 1))); do
    ./run.sh $IDX
    cp -v -r "$IMGS_PATH/transfer_plots" "$IMGS_PATH/transfer_plots_$IDX"
done
