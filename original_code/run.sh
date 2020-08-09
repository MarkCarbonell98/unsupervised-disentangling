#! /usr/bin/env bash



python "$(dirname "$0")/predict-demo.py" baseline_deepfashion_256 \
--dataset deepfashion --bn 1 --static \
--in_dim 256 \
--reconstr_dim 256 \
--covariance \
--contrast_var 0.01 \
--brightness_var 0.01 \
--saturation_var 0.01 \
--hue_var 0.01 \
--adversarial \
--mode infer \
--pck_tolerance 6 2>&1 | grep -Evi 'warning'
