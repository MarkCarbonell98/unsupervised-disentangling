import cv2
import numpy as np
import sys
import os

n = int(sys.argv[1])

def merge_all_transfers(path="experiments/baseline_deepfashion_256/transfer_plots", n_transfers = n, save_dir="experiments/baseline_deepfashion_256/all_transfer_plots"):
    first_filename = path + "_-1/transfer_plot.png"
    m = cv2.imread(first_filename)
    for i in range(n_transfers):
        filename = path + "_" + str(i) +  "/transfer_plot.png"
        transfer_plot = cv2.imread(filename)
        m = np.vstack((m, transfer_plot))
        print(m.shape)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    save_path = save_dir + "/all_transfer_plots.png"
    cv2.imwrite(save_path, m)

merge_all_transfers()
