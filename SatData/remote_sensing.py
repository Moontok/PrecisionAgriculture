import rasterio
import numpy as np
import matplotlib.pyplot as plt


def plot_rgb(red_band_path, green_band_path, blue_band_path):
    """RGB (Red-Green-Blue):
    This is the most common way to visualize color images.
    It combines the red, green, and blue bands into a single image.

    The red band is used for the red channel, the green band for the green channel,
    and the blue band for the blue channel.
    """
    
    with rasterio.open(red_band_path) as red_band:
        with rasterio.open(green_band_path) as green_band:
            with rasterio.open(blue_band_path) as blue_band:
                red = red_band.read(1).astype(float)
                green = green_band.read(1).astype(float)
                blue = blue_band.read(1).astype(float)
                rgb = np.dstack((red, green, blue))
        rgb = rgb / rgb.max()
    plt.imshow(rgb)
    plt.title('RGB from Landsat Imagery')
    plt.show()


def plot_ndvi(red_band_path, nir_band_path):
    """NDVI (Normalized Difference Vegetation Index):
    This is the most widely used VI.
    It measures the difference between near-infrared (NIR) and red reflectance,
    indicating the density and health of green vegetation.
    Higher NDVI values generally indicate healthier vegetation.

    NDVI = (NIR - Red) / (NIR + Red)
    """
    with rasterio.open(red_band_path) as red_band:
        with rasterio.open(nir_band_path) as nir_band:
            red = red_band.read(1).astype(float)
            nir = nir_band.read(1).astype(float)            
            ndvi = (nir - red) / (nir + red)
    plt.imshow(ndvi, cmap='RdYlGn')
    plt.colorbar(label='NDVI')
    plt.title('NDVI from Landsat Imagery')
    plt.show()


def plot_gndvi(green_band, nir_band):
    """GNDVI (Green Normalized Difference Vegetation Index):
    This is a vegetation index that minimizes soil brightness influences.
    It is particularly useful in areas with high soil brightness.
    It compares the green and near-infrared (NIR) bands.

    GNDVI = (NIR - Green) / (NIR + Green)
    """

    with rasterio.open(green_band) as green_band:
        with rasterio.open(nir_band) as nir_band:
            green = green_band.read(1).astype(float)
            nir = nir_band.read(1).astype(float)
            gndvi = (nir - green) / (nir + green)
    plt.imshow(gndvi, cmap='RdYlGn')
    plt.colorbar(label='Green Normalized Difference Vegetation Index (GNDVI)')
    plt.title('GNDVI from Landsat Imagery')
    plt.show()


def plot_ndmi(swir1_band, nir_band):
    """NDMI (Normalized Difference Moisture Index):
    This is a vegetation index that is sensitive to moisture content.
    It compares the near-infrared (NIR) and shortwave infrared (SWIR) bands.

    NDMI = (NIR - SWIR1) / (NIR + SWIR1)
    """

    with rasterio.open(nir_band) as nir_band:
        with rasterio.open(swir1_band) as swir1_band:
            nir = nir_band.read(1).astype(float)
            swir1 = swir1_band.read(1).astype(float)
            msi = (nir - swir1) / (nir + swir1)
    plt.imshow(msi, cmap='RdYlGn')
    plt.colorbar(label='NDWI')
    plt.title('NDWI from Landsat Imagery')
    plt.show()


def plot_ndwi(green_band, nir_band):
    """NDWI (Normalized Difference Water Index):
    This is a vegetation index that is sensitive to water content.
    It compares the green and near-infrared (NIR) bands.

    NDWI = (Green - NIR) / (Green + NIR)
    """

    with rasterio.open(green_band) as green_band:
        with rasterio.open(nir_band) as nir_band:
            green = green_band.read(1).astype(float)
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
# plot_ndvi(red_band, nir_band)
# plot_gndvi(green_band, nir_band)
# plot_ndmi(swir1_band, nir_band)
plot_ndwi(green_band, nir_band)


