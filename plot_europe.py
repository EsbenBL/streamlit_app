import geopandas as gpd
import requests
import matplotlib.pyplot as plt


def plot_europe():
    eu_data = gpd.read_file("https://raw.githubusercontent.com/leakyMirror/map-of-europe/master/GeoJSON/europe.geojson")
    eu_data = eu_data.to_crs(31287)
    eu_data.head()


    # Filter 
    eu_data = eu_data[-eu_data.NAME.isin(["Russia", "Iceland", "Turkey", "Israel", "Azerbaijan", "Georgia", "Armenia"])]

    fig, ax = plt.subplots(1,1, figsize = (10,10))

    ax.set_axis_off()

    eu_data.plot(ax=ax, color = "#E5E7E9", edgecolor = "White", linewidth = 0.5)
    eu_data[eu_data.NAME.isin(["Denmark"])].plot(ax=ax, color = "#64f0af", linewidth = 0.5)
    eu_data[eu_data.NAME.isin(["Sweden", "Netherlands"])].plot(ax=ax, color = "#c3fae1", linewidth = 0.5)

    return fig 