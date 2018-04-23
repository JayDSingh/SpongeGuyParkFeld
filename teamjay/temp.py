import nltk
import re
from collections import defaultdict
import csv

data = defaultdict(list)

regex_line = r"^.+: *"
regex_speaker = r":.+$"

# preprocessing -- extracting speaker name, making it key
# extracting line, making it part of speaker list
def pre(line):

    text = re.split(regex_line, line)[1]

    print(text)

    speaker = re.split(regex_speaker, line)[0].lower()

    print(speaker)
    
    data[speaker] += [text]


# this is not how it is done... 
# want to read csv, go row by row, add each line's speaker/text to dictionary
thing = csv.reader("C:/Users/Lauren Shin/Documents/github/SpongeGuyParkFeld/teamjay/scripts.csv")

for row in thing:
    pre(row)

print(data)