from PIL import Image
import numpy as np
import os
import unittest

matrix = np.array((256 * 9, 256 * 9, 3)

def getImages(path):
    "Returns all images found in path as a numpy array"
    base = np.array([])
    for img in os.listdir(path):
        image = np.asarray(Image.open(path + "/" + img), dtype="int32"), axis=1
        np.hstack((matrix, image))
    # images = [np.asarray(Image.open(path + "/" + img), dtype="int32") for img in os.listdir(path)]
    pass


getImages('./experiments/baseline_deepfashion_256/images')
# getImages('./experiments/baseline_deepfashion_256/images_kps')
# getImages('./experiments/baseline_deepfashion_256/images_transfer')

class TransferPlotTest(unittest.TestCase):

    def testGetImages(self):
        self.assertEqual(getImages('asdfadf'), None)
        self.assertEqual

