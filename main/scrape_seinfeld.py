# attempt at grabbing all the urls for seinfeld scripts
# and writing them to a csv file
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import re

# url with all the episode links
transcripts = "http://www.seinfeldscripts.com/seinfeld-scripts.html"
# opens url and reads html contents
rawHTML = urlopen(transcripts).read()

# makes beautiful soup object and parses html from opened url
soup = BeautifulSoup(rawHTML, "html.parser")

links = []

# looks through each 'a' tag in the second table in the webpage
for link in soup.find_all("table")[1].find_all("a"):
    # strips string of whitespace (some have intitial spaces)
    # and concatenates it with homepage url to form the full url
    # adds it to the list of links
    links += ["http://www.seinfeldscripts.com/" + link.get("href").strip()]

# create csv file
with open('temp_seinfeld_transcript.csv', 'w', encoding = 'utf-8') as csvfile:
    filewriter = csv.writer(csvfile, delimiter = ',', quoting=csv.QUOTE_ALL, quotechar='"')
    filewriter.writerow(["Character", "Line"])

    episode_number = 1
    for single_link in links:
        episode_number += 1
        # soup_tester.py
        # url to look at
        # opens url and reads html contents
        firstHTML = urlopen(single_link).read()

        # makes beautiful soup object and parses html from opened url
        soup = BeautifulSoup(firstHTML, "html.parser")

        # matches for this episode
        matches = []
        # scraping data from pages
        for entry in soup.find("div", {"id": "content"}):
            # searches each entry for a match
            # regex explanation:
            # ^ start of string
            # [^\s]* does not match any number of whitespace characters
            # [\w]+ has 1+ of word character(s) (a-z, A-Z, 0-9)
            # [\s]* has 0 to unlimimted whitespace
            # : matches exactly
            # (?=\s*\w) positive lookahead (?)
            # \s* any number of whitespaces
            # \w any word character
            # original ^[^\s]*[\w]+[\s]*:(?=\s*\w)
            # .+ any character one or more times
            # re.DOTALL -- . matches everything, even newline characters

            match = re.search(r"^[^\s]*[\w]+[\s]*:.+", str(entry), re.DOTALL)

            if (match != None):
                # removes p tags
                clean = re.sub(r"<\/*p>", "", match.group(0))
                # removes lines with brackets
                cleaner = re.sub(r'[\(\[].*?[\)\]]', "", clean, flags = re.S)
                # adds cleaned string to list
                final = cleaner.split(':')

                final[0] = final[0].lower();

                filewriter.writerow(final)

        # writes csv with cleaned strings


input_file = open("temp_seinfeld_transcript.csv", "r", encoding="utf8")
with open('seinfeld_transcript.csv', 'w', newline='', encoding='utf-8') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    for row in csv.reader(input_file):
        if len(row)>0:
            if len(row)>= 2:
                line = row[1]
            else:
                line = ''
            for i in range(2,len(row)):
                line += row[i]
            L = [row[0],line]
            spamwriter.writerow(L)
