# attempt at grabbing all the urls for seinfeld scripts
from bs4 import BeautifulSoup
from urllib.request import urlopen

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

print(links)

#######################################################################
#
# # other random stuff
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

#######################################################################

# to do things for each page:
# get rid of stage directions
# pair speaker names with dialogue + get rid of semicolon
# get episode and season numbers
# CSV -- season, episode, character, line
# don't catch start and end of episode, probably look at table element only