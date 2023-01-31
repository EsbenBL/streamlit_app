
import geopandas as gpd
import json
import requests
import pandas as pd 
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np 


def plot_dk():
    #Henter geo-info om de danske kommuner
    url = "https://raw.githubusercontent.com/ok-dk/dagi/master/geojson/kommuner.geojson"
    kommuner = gpd.read_file(url)

    #Set to meter based system
    kommuner.to_crs(epsg = '25832', inplace = True)

    kommuner.columns = kommuner.columns.str.lower()
        
    # information for municipality
    kommune_info = pd.read_json('https://dawa.aws.dk/kommuner')\
                    .pipe(lambda df: \
                            df.assign(komkode=df.kode.astype(str).str.zfill(4)))\
                    .loc[:,['komkode', 'regionskode']]\
                    

    region_info = pd.read_json('https://dawa.aws.dk/regioner/')\
                    .loc[:,['kode','navn']]\
                    .add_prefix('regions')

    kommuner = kommuner\
                    .merge(kommune_info,how='left')\
                    .merge(region_info,how='left')

    kommuner.rename(columns = {"komnavn":"Kommune"}, inplace = True)

    # Match spelling to DST-standard
    kommuner.Kommune = np.where(kommuner.Kommune == "Høje Taastrup",
                        "Høje-Taastrup",
                        kommuner.Kommune)

    kommuner = kommuner.query("Kommune != 'Christiansø'")

    print(len(kommuner))
    kommuner.head()


    fig, ax = plt.subplots(1,1, figsize = (10,10))

    sub_axes = inset_axes(ax,
                            width="15%", # width = 30% of parent_bbox
                            height="15%", # height : 1 inch
                            loc = "upper right")


    geo_plot = kommuner.copy()

    bornholm = geo_plot.query("Kommune == 'Bornholm'")
    geo_plot = geo_plot.query("Kommune != 'Bornholm'")


    ax = geo_plot.plot(ax=ax, legend = False, color="#64f0af", edgecolor =  "#64f0af", linewidth=.7)

    ax.set_axis_off();

    sub_axes = bornholm.plot(ax=sub_axes, color="#64f0af", edgecolor =  "#64f0af", linewidth=.1)

    sub_axes.set_xticks([])
    sub_axes.set_yticks([])

    return fig