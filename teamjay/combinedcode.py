# read in every episode of seinfeld script to csv file

# attempt at grabbing all the urls for seinfeld scripts
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import re

# soup.py
# url to look at
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
with open('scripts.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter = '\n', quoting=csv.QUOTE_ALL, quotechar='"')
    filewriter.writerow(['Season Episode Character Dialogue'])

    for single_link in links[0:5]:
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

            print(entry)
            match = re.search(r"^[^\s]*[\w]+[\s]*:.*<\/p>", str(entry))

            if (match != None):
                # regex to remove p tags
                clean = re.sub(r"<\/*p>", "", match.group(0))
                cleaner = re.sub(r"[\(\[].*?[\)\]]", "", clean)
                matches += [cleaner]

        filewriter.writerow(matches)


