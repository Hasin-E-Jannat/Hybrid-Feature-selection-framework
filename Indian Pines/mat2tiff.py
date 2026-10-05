import scipy.io
import rasterio
import numpy as np

# Load .mat files
hyperspectral_data = scipy.io.loadmat("Indian_pines_corrected.mat")["indian_pines_corrected"]  # Hyperspectral data
#labels_data = scipy.io.loadmat("Indian_pines_gt.mat")["indian_pines_gt"]  # Ground truth labels

# Save hyperspectral data as .tif
with rasterio.open(
    "indian_pines_image.tif",
    "w",
    driver="GTiff",
    height=hyperspectral_data.shape[0],
    width=hyperspectral_data.shape[1],
    count=hyperspectral_data.shape[2],
    dtype=np.float32,
) as dst:
    for i in range(hyperspectral_data.shape[2]):
        dst.write(hyperspectral_data[:, :, i], i + 1)
'''

# Save labels as .tif
with rasterio.open(
    "indian_pines_labels.tif",
    "w",
    driver="GTiff",
    height=labels_data.shape[0],
    width=labels_data.shape[1],
    count=1,
    dtype=np.int32,
) as dst:
    dst.write(labels_data, 1)
'''
print("Conversion complete! Files saved as 'indian_pines_image.tif' and 'indian_pines_labels.tif'.")
