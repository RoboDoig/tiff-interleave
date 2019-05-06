import os
import glob
from skimage.external.tifffile import imread, imsave, TiffFile
import matplotlib.pyplot as plt
import numpy as np

path = 'X:/2p/190402/TSeries-04022019-1623-009'

im_files = glob.glob(os.path.join(path, '*.tif'))

# reshape
master_file = imread(im_files[0])
dims = master_file.shape
reshaped = np.reshape(master_file, (dims[0]*2, dims[2], dims[3]))

os.mkdir(os.path.join(path, 'Combined'))
imsave(os.path.join(path, 'Combined', 'combined.tif'), reshaped)
