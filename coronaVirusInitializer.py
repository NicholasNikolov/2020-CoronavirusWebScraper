# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 23:13:42 2020

@author: nikol
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import numpy as np
from os import listdir

extractTime = datetime.datetime.now()
extractTime = str(extractTime)
print("Access Initiated at " + extractTime)
link = 'https://www.worldometers.info/coronavirus/'
response = requests.get(link)
soup = BeautifulSoup(response.text,'html.parser').findAll('td')#[1107].get_text()


table = pd.DataFrame(columns=['Date and Time','Country','Total Cases','New Cases','Total Deaths','New Deaths','Total Recovered','Active Cases','Serious Critical','Total Cases/1M pop','Total Deaths/1M pop','Total Tests','Total Tests/1M pop'])
soupList = []

for i in range(2484):
    value = soup[i].get_text()
    soupList.insert(i,value)

soupList = [x.strip(' ') for x in soupList]

    

table = np.reshape(soupList,(207,12))
table = pd.DataFrame(table)
table.columns=['Country','Total Cases','New Cases (+)','Total Deaths','New Deaths (+)','Total Recovered','Active Cases','Serious Critical','Total Cases/1M pop','Total Deaths/1M pop','Total Tests','Total Tests/1M pop']
table['Date & Time'] = extractTime


#Below code is run once to generate the initial files. That's it.

for i in range(207):
    fileName = table.iloc[i,0] + '.csv'
    table.iloc[i:i+1,:].to_csv(fileName)


FilesDirectory = 'D:\\Professional\\Coronavirus'
fileType = '.csv'
filenames = listdir(FilesDirectory)
DataFiles = [ filename for filename in filenames if filename.endswith(fileType) ]


for file in DataFiles:
    countryData = pd.read_csv(file)
    MatchedCountry = table.loc[table['Country'] == str(file)[:-4]]
    countryData = countryData.append(MatchedCountry)
    countryData.to_csv(FilesDirectory + '\\'+str(file))