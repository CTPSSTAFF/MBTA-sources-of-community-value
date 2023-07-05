import geopandas as gpd
import fiona
import numpy as np
import pandas as pd

core_url = "https://services1.arcgis.com/ceiitspzDAHrdGO1/arcgis/rest/services/Core_Service_Area/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"
extend_url = "https://services1.arcgis.com/ceiitspzDAHrdGO1/arcgis/rest/services/MBTA_Extended_Service_Area/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"
data_dir = "C:/Users/bbact/Documents/GitHub/MBTA-sources-of-community-value/Data/"

core_area = gpd.read_file(core_url)
extend_area = gpd.read_file(extend_url)
growth = pd.read_excel(data_dir + "New growth by town/new_growth_town_FY2003_FY2023.xls")
massbuilds = gpd.read_file(data_dir + "massbuilds_June28/massbuilds-shp-20230628-264e49.shp")

core_area['town_name'] = core_area['TOWN'].str.capitalize()
extend_area['town_name'] = extend_area['TOWN'].str.capitalize()

# find percent of massbuilds that are in core service area, extended service area, 




