# Inofficial steps to reproduce the results

* I tried many ways to reproduce the results and found that the following parameters work well.


## Deepfashion

* Deepfashion is trained on single images, so it is a *static* dataset.

```bash
export CUDA_VISIBLE_DEVICES=X # instead of main.py --gpu xx
python main.py baseline_deepfashion_256 \
--dataset deepfashion --mode train --bn 8 --static \
--in_dim 256 \
--reconstr_dim 256 \
--covariance \
--pad_size 25 \
--contrast_var 0.01 \
--brightness_var 0.01 \
--saturation_var 0.01 \
--hue_var 0.01 \
--adversarial \
--c_precision_trans 0.01
```

* Note that I had to make a custom split of the data for Deepfashion, which is basically going through all the data in the 
in-shop subset of Deepfashion and filter out those images where all keypoints are visible.
* To get the keypoints, I simply used Alpha Pose.
* The custom subset is released under [custom_datasets/deepfashion](custom_datasets/deepfashion/README.md)


A pretrained checkpoint is available [here](https://heibox.uni-heidelberg.de/f/c2e7b6a77f2f4736a01f/?dl=1).