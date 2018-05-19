#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 19:30:00 2018

@author: Mikki
"""
import nltk
import re
from collections import defaultdict
import csv
import string

data = defaultdict(list)

regex_speaker = r"^.{1,10}: *"
regex_line = r":.+$"

# preprocessing -- extracting speaker name, making it key
# extracting line, making it part of speaker list
def pre(line):

    text = re.search(regex_line, line)
    speaker = re.search(regex_speaker, line)

    if (text and speaker):
        # need to clean these up... not very good regexes...
        speaker = re.sub("\W{2,}", "", speaker.group(0).lower())
        text = re.sub("\s{2,}", "", text.group(0).lower())
        data[speaker] += [text]

with open('seinfeld_transcript.csv', encoding="utf-8") as csvfile:
    csvFile = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvFile:
        pre(str(row))

with open('new_seinfeld_transcript.csv', 'w', encoding="utf-8") as csvfile:
    filewriter = csv.writer(csvfile, delimiter = '\n', quoting=csv.QUOTE_ALL, quotechar='"')
    for key, value in data.items():
        row = str(key, ",", str(data[key])
        filewriter.writerow(row)
