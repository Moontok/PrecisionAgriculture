#https://www.earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/landsat-in-Python/

import os
from glob import glob

import matplotlib.pyplot as plt
import geopandas as gpd
import rasterio as rio
import xarray as xr
import rioxarray as rxr
import numpy as np
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
from shapely.geometry import mapping


def open_clean_bands(band_path):
    return rxr.open_rasterio(band_path, masked=True).squeeze()

all_landsat_post_bands = glob(os.path.join("data", "*T1_B*.TIF"))
all_landsat_post_bands.sort()


band_1 = open_clean_bands(all_landsat_post_bands[4])

ep.plot_bands(band_1 , scale=False)

plt.show()

