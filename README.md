# ICE Extract Data
# Overview
This application extracts public data from Intercontinental Exchange (ICE) for clearable credit default swap (CDS) products. In particular the application will extract the data for the latest 5Y tenor series of the following:<br>
* CDX NA IG
* CDX NA HY
* CDX EM
* EUR iTraxx Main
* EUR iTraxx Crossover

# Requirements
Application requires Python3 and the following packages:<br>
* requests
* datetime
* pandas
* xlrd

# Output 
Application will save the file extracted from ICE page in Folder ICE_Files in the format yyyy.mm.dd_ICE_File.xls<br>
Application will also save the latest series for the products detailed in the Overview in the Output folder in the format yyyy.mm.dd_ICE.output.csv
# Run
To run applicaton in the Terminal type `python3 ICE_extract_data.py`
