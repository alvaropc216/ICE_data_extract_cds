#!/usr/bin/env python3
# By:Alvaro Peredo Centellas
# Date:2020-10-11
# Version: 1.0
# Import packages
import requests
from datetime import date
import pandas as pd

# Imports Excel File from ICE Page
url = "https://www.theice.com/publicdocs/clear_credit/ICE_Clear_Credit_Clearing_Eligible_Products.xls"
resp = requests.get(url)

today = date.today()
file_name_today = F'ICE_File/{today.year}.{today.month}.{today.day}_ICE_File.xls'
output = open (file_name_today,'wb')
output.write(resp.content) #need to install package xlrd for Python3
output.close()

# Read tabs corresponding for CDX, CDX EM, EUIR iTRaxx Indices
usd_cdx_indices = pd.read_excel(file_name_today, 'US CDX Indices',skiprows=3)
usd_cdx_indices = usd_cdx_indices.rename(columns = {'Required for Clearing*':'Required for Clearing'}) #renaming column to match others
usd_cdxem_indices = pd.read_excel(file_name_today,'CDX EM Indices',skiprows=3)
eur_itraxx_indices = pd.read_excel(file_name_today,'EUR iTraxx Indices', skiprows=3)
eur_itraxx_indices = eur_itraxx_indices.rename(columns = {'Required for Clearing*':'Required for Clearing'}) #renaming column to match others

#For CDX US extracts the latest 5Y for IG and HY
usd_cdx_ig = usd_cdx_indices.loc[(usd_cdx_indices['Index Family']=='IG')&\
                                 (usd_cdx_indices['Index Tenor']=='5Y')]
usd_cdx_nig = usd_cdx_indices.loc[(usd_cdx_indices['Index Family']=='High Yield')&\
                                 (usd_cdx_indices['Index Tenor']=='5Y')]

#For CDX EM Indices extract latest
usd_cdxem_5y = usd_cdxem_indices.loc[usd_cdxem_indices['Index Tenor']=='5Y']

#For ITRAXX Europe extract latest ofr Itraxx and Crossover
eur_simple_itraxx = eur_itraxx_indices.loc[(eur_itraxx_indices['Index Family']=='Main')\
                                            &(eur_itraxx_indices['Index Tenor']=='5Y')]
eur_crossover_itraxx = eur_itraxx_indices.loc[(eur_itraxx_indices['Index Family']=='Crossover')\
                                            &(eur_itraxx_indices['Index Tenor']=='5Y')]

#Combine latest data for Credit products and creates CSV file in Output folder
combined_dataset = pd.concat([usd_cdx_ig[-1:],usd_cdx_nig[-1:],\
                              usd_cdxem_5y[-1:],eur_simple_itraxx[-1:],\
                              eur_crossover_itraxx[-1:]],ignore_index=True)
combined_dataset.to_csv(F'Output/{today.year}.{today.month}.{today.day}_ICE_output.csv')
