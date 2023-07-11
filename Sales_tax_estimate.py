import geopandas as gpd
import fiona
import numpy as np
import pandas as pd

core_url = "https://services1.arcgis.com/ceiitspzDAHrdGO1/arcgis/rest/services/Core_Service_Area/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"
extend_url = "https://services1.arcgis.com/ceiitspzDAHrdGO1/arcgis/rest/services/MBTA_Extended_Service_Area/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"
data_dir = "C:/Users/bbact/Documents/GitHub/MBTA-sources-of-community-value/Data/"

core_area = gpd.read_file(core_url)
extend_area = gpd.read_file(extend_url)
def annual_tax(year):
    types = {'January':'int64','February':'int64','March':'int64','April':'int64','May':'int64','June':'int64','July':'int64',
            'August':'int64','September':'int64','October':'int64','November':'int64','December':'int64'}
    tax = pd.read_excel(data_dir + "Sales tax/dor-2019-2022-sales-use-tax-revenue-collections-by-city-town.xlsx",sheet_name=year,dtype=types)

    tax['tax_year'] = tax[['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']].sum(axis=1)
    tax = tax.drop(columns=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    # sales tax is 6.25%
    tax['sales'] = tax['tax_year'] / 0.0625
    return tax

tax = annual_tax("2022")

#Note: MBTA recieves an additional 160,000,000 annually

# 2022
total_tax = sum(tax['tax_year']) # 6,355,380,949
total_sales = sum(tax['sales']) # 101,686,095,184
total_to_mbta = total_tax * 0.16 # 1,016,860,951.84

# 2021
total_tax = sum(tax['tax_year']) # 5,921,361,987
total_sales = sum(tax['sales']) # 94,741,791,792
total_to_mbta = total_tax * 0.16 # 947,417,917.92

# 2020
total_tax = sum(tax['tax_year']) # 5,131,647,211
total_sales = sum(tax['sales']) # 82,106,355,376
total_to_mbta = total_tax * 0.16 # 821,063,553.76

# 2019
total_tax = sum(tax['tax_year']) # 4,850,026,981
total_sales = sum(tax['sales']) # 77,600,431,696
total_to_mbta = total_tax * 0.16 # 776,004,316.96

core_area['town_name'] = core_area['TOWN'].str.capitalize()
extend_area['town_name'] = extend_area['TOWN'].str.capitalize()

tax['Town'] = tax['Town'].apply(lambda x: x.split(' ', 1)[-1])

core_tax = pd.merge(core_area,tax,left_on='town_name',right_on='Town')
extend_tax = pd.merge(extend_area,tax,left_on='town_name',right_on='Town')

def more_tax(core_tax=core_tax,extend_tax=extend_tax,tax=tax,rate=0):
    rate_ratio = rate / 100
    core_tax['new_tax'] = core_tax['sales'] * rate_ratio
    extend_tax['new_tax'] = extend_tax['sales'] * rate_ratio
    tax['new_tax'] = tax['sales'] * rate_ratio

    core_sum = round(sum(core_tax['new_tax']),0)
    extend_sum = round(sum(extend_tax['new_tax']),0)
    tax_sum = round(sum(tax['new_tax']),0)
    return [rate,core_sum,extend_sum,tax_sum]


print(more_tax(rate=.1))
print(more_tax(rate=.25))
print(more_tax(rate=.5))
print(more_tax(rate=.75))
print(more_tax(rate=1))


