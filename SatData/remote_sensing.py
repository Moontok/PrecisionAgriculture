import rasterio as rio
import numpy as np
import matplotlib.pyplot as plt


def plot_rgb(r_path, g_path, b_path):
    """RGB (Red-Green-Blue):
    This is the most common way to visualize color images.
    It combines the red, green, and blue bands into a single image.

    The red band is used for the red channel, the green band for the green channel,
    and the blue band for the blue channel.
    """
    
    with rio.open(r_path) as red_band:
        red = red_band.read(1).astype(float)
    with rio.open(g_path) as green_band:
        green = green_band.read(1).astype(float)
    with rio.open(b_path) as blue_band:
        blue = blue_band.read(1).astype(float)

    rgb = np.dstack((red, green, blue))
    rgb = rgb / rgb.max()
    
    plt.imshow(rgb)
    plt.title('RGB from Landsat Imagery')
    plt.show()


def plot_ndvi(r_path, nir_path):
    """NDVI (Normalized Difference Vegetation Index):
    This is the most widely used VI.
    It measures the difference between near-infrared (NIR) and red reflectance,
    indicating the density and health of green vegetation.
    Higher NDVI values generally indicate healthier vegetation.

    NDVI = (NIR - Red) / (NIR + Red)
    """
    with rio.open(r_path) as red_band:
        red = red_band.read(1).astype(float)
    with rio.open(nir_path) as nir_band:
        nir = nir_band.read(1).astype(float)            
    
    ndvi = (nir - red) / (nir + red)

    plt.imshow(ndvi, cmap='RdYlGn')
    plt.colorbar(label='NDVI')
    plt.title('NDVI from Landsat Imagery')
    plt.show()


def plot_gndvi(g_path, nir_path):
    """GNDVI (Green Normalized Difference Vegetation Index):
    This is a vegetation index that minimizes soil brightness influences.
    It is particularly useful in areas with high soil brightness.
    It compares the green and near-infrared (NIR) bands.

    GNDVI = (NIR - Green) / (NIR + Green)
    """

    with rio.open(g_path) as g_path:
        green = g_path.read(1).astype(float)
    with rio.open(nir_path) as nir_path:
        nir = nir_path.read(1).astype(float)
    
    gndvi = (nir - green) / (nir + green)

    plt.imshow(gndvi, cmap='RdYlGn')
    plt.colorbar(label='Green Normalized Difference Vegetation Index (GNDVI)')
    plt.title('GNDVI from Landsat Imagery')
    plt.show()


def plot_ndmi(swir1_path, nir_path):
    """NDMI (Normalized Difference Moisture Index):
    This is a vegetation index that is sensitive to moisture content.
    It compares the near-infrared (NIR) and shortwave infrared (SWIR) bands.

    NDMI = (NIR - SWIR1) / (NIR + SWIR1)
    """

    with rio.open(nir_path) as nir_path:
        nir = nir_path.read(1).astype(float)
    with rio.open(swir1_path) as swir1_path:
        swir1 = swir1_path.read(1).astype(float)
    
    ndmi = (nir - swir1) / (nir + swir1)

    plt.imshow(ndmi, cmap='RdYlGn')
    plt.colorbar(label='NDMI')
    plt.title('NDMI from Landsat Imagery')
    plt.show()


def plot_ndwi(g_band, nir_band):
    """NDWI (Normalized Difference Water Index):
    This is a vegetation index that is sensitive to water content.
    It compares the green and near-infrared (NIR) bands.

    NDWI = (Green - NIR) / (Green + NIR)
    """

    with rio.open(g_band) as g_band:
        green = g_band.read(1).astype(float)
    with rio.open(nir_band) as nir_band:
        nir = nir_band.read(1).astype(float)

    ndwi = (green - nir) / (green + nir)

    plt.imshow(ndwi, cmap='RdYlGn')
    plt.colorbar(label='NDWI')
    plt.title('NDWI from Landsat Imagery')
    plt.show()


blue_band = "may_data/B2.TIF"
green_band = "may_data/B3.TIF"
red_band = "may_data/B4.TIF"
nir_band = "may_data/B5.TIF"
swir1_band = "may_data/B6.TIF"

# plot_rgb(red_band, green_band, blue_band)
plot_ndvi(red_band, nir_band)
# plot_gndvi(green_band, nir_band)
# plot_ndmi(swir1_band, nir_band)
# plot_ndwi(green_band, nir_band)


