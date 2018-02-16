# systematically grabbing all the urls for seinfeld scripts
# the seinfeld-scripts page has all the page names in a table
# so that's probably the best way to get them all

from bs4 import BeautifulSoup
from urllib.request import urlopen

# url to look at
transcripts = "http://www.seinfeldscripts.com/seinfeld-scripts.html"
# opens url and reads html contents
rawHTML = urlopen(transcripts).read()

# makes beautiful soup object and parses html from opened url
soup = BeautifulSoup(rawHTML, "html.parser")

# print(soup)

links = []

# looks through each 'a' tag in the second table in the webpage
# first table has advertisements, while the second has the links to scripts
for link in soup.find_all("table")[1].find_all("a"):
    # strips string of whitespace (some have intitial spaces)
    # and concatenates it with homepage url to form the full url
    # adds it to the list of links
    links += ["http://www.seinfeldscripts.com/" + link.get("href").strip()]

# print(links)

# print(type(link))

# scraping data from pages
<<<<<<< HEAD
import re

# starting with smaller subset for testing purposes
=======
# starting with smaller subset for testing purposes
import re

>>>>>>> a23a6eea2e6f1ec48d20f0ea2f950626aeb05f2b
for url in links[0:1]:
    # opens the url's html
    temp_html = urlopen(url).read()
    # parses html into soup object
    temp_soup = BeautifulSoup(temp_html, "html.parser")
<<<<<<< HEAD
    # finding the first speaker name with regex
    # finds all p tags in the div element
    for entry in temp_soup.find("div", {"id": "content"}).find_all("p"):
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
        match = re.search(r"^[^\s][\w]+[\s]*:(?=\s*\w)", str(entry))
        # print(match)
=======
    # prints text of div and p tags
    # finding the first speaker name with regex
    # does not currently work
    # might have to loop through list
    match = re.search(r"(?<=[\w]{1}):(?=\s*\w)", temp_soup.find("div", {"id": "content"}).find_all("p"))
    # regex to find 
    # "<p>charcharcharnospace: wordswordswords"
    # ie first character name
>>>>>>> a23a6eea2e6f1ec48d20f0ea2f950626aeb05f2b


#####################################################################
# notes about scripts/inconsistencies
# not all paragraphs are a new speaker, sometimes just a new line
# some scripts have words before script, ie characters, writers
# stage directions with [] or % 
# 
#####################################################################
# # other random stuff
# # old code for reference if needed, not part of project
#
# # script url
# url = "http://www.seinfeldscripts.com/seinfeld-scripts.html"
# # reads html
# html = urlopen(url).read()
# # print(html)
#
# soup = BeautifulSoup(html, "html.parser")
#
# # finding links
# for link in soup.find_all('a'):
#      print(link.get('href'))
#     # prints PageName.htm
#     # not full url
#     # and there is also whitespace front that's probably problematic
#
# for string in soup.stripped_strings:
#     print(repr(string))

######################################################################
# to do things for each page:
# get rid of stage directions
# pair speaker names with dialogue + get rid of semicolon
# get episode and season numbers
# CSV -- season, episode, character, line
# don't catch start and end of episode, probably look at table element only