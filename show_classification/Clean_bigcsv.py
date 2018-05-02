""" This script cleans the merged csv, `mergedbigcsv.csv`.
    The goal here is to get a big bag of lines sorted by character for all of
    the spongebob episodes in this document.
    The idea is that we have a list for each character, e.g. 'spongebob_all_lines' that contains
    all of spongebob's lines in this dataset.
"""
#  4/30/18
#  Author: Evan Azevedo
#  Future work:
#  Improve on character list to get an accurate list of Spongebob characters.
#  Get the lines with episode numbers and season numbers to improve
#+ granulariy.


import csv

#  Let's read the csv file
with open('mergedbigcsv.csv', 'r', newline='', encoding='utf-8') as csvfile:
    all_lines = []
    for row in csv.reader(csvfile, delimiter=','):
        all_lines.append(row)
        #  Now all_lines is a list where each line in the csv is a list

#  Lets remove all of the blank elements, and strip off whitespace
filtered = []
for line in all_lines:
    stripped = map(str.strip, line)
    content = list(filter(None, stripped))
    filtered.append(content)

##  We also need to remove blank all_lines
clean = list(filter(None, filtered))
#print(clean)

#  get a list of the characters.
characters = [item[0] for item in clean]
#  print all unique characters with set()
print(len(set(characters)))
##  Using this script, we get 1891 unique characters...
##  Obviously, some of these are actual lines
## One of them I saw was even a song.
