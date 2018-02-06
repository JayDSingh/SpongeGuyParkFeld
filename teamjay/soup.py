# random stuff with beautiful soup

from bs4 import BeautifulSoup
from urllib.request import urlopen

# url to look at
firstEpi = "http://www.seinfeldscripts.com/TheSeinfeldChronicles.htm"
# opens url and reads html contents
firstHTML = urlopen(firstEpi).read()

# makes beautiful soup object and parses html from opened url
stew = BeautifulSoup(firstHTML, "html.parser")

# extracts scripts from html
for script in stew(["script", "style"]):
    script.extract()

# english without html
# words = stew.get_text()
    # different from stew.get_text
# print(words)

# prints the contents of the first div element in html
print(stew.find("div", {"id": "content"}))

#######################################################################
#
# # other stuff, basically same thing as above?
#
# # first episode script url
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