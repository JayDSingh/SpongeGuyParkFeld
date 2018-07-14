#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 16:33:18 2018

@author: Mikki
"""
#Creating a dictionary with key-value pairs representing each row
#with [Season, Episode, and Character] as the key and the Line as the value

from collections import defaultdict
SouthParkDict = {}

import csv
import pandas as pd
SouthPark_df = pd.read_csv('/Users/Mikki/Desktop/Data Science/Winter 2018/All-seasons.csv',
                           na_values=['.'])

for row in SouthPark_df:
    metadata = []
    metadata += [SouthPark_df['Season']]
    metadata += [SouthPark_df['Episode']]
    metadata += [SouthPark_df['Character']]
    SouthPark_lines = SouthPark_df['Line']
    SouthPark_lines = SouthPark_lines.to_string()
    #I was trying to turn each Line into a list of all the words in each line;
    #It did not go as expected
    SouthPark_lines = SouthPark_lines.split()
    #Attempting to add to the dictionary yields TypeError: unhashable type: 'list'
    SouthParkDict[SouthPark_lines] += [metadata]

#print(SouthParkDict)