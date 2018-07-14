from bs4 import BeautifulSoup
from urllib.request import urlopen

# url to look at
transcripts = "http://spongebob.wikia.com/wiki/List_of_transcripts#Season"
# opens url and reads html contents
rawHTML = urlopen(transcripts).read()

# makes beautiful soup object and parses html from opened url
soup = BeautifulSoup(rawHTML, "html.parser")

links = []

#looks through each 'a' tag in the second table in the webpage
for joup in soup.find_all("table"):
    pinks = joup.find_all("a")
    for pink in pinks:
    # strips string of whitespace (some have intitial spaces)
    # and concatenates it with homepage url to form the full url
    # adds it to the list of links
        links += ["http://spongebob.wikia.com/wiki/" + pink.get("href").strip()]

for i in range(868,len(links)):
    links.pop()

linksrem = []
for i in range(867):
    if i%2 == 0:
        linksrem.append(links[i])

for i in linksrem:
    ind = links.index(i)
    links.pop(ind)

print(links)

