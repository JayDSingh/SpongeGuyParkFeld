#compiles all the transcript links from season 1 into a list

from bs4 import BeautifulSoup
from urllib.request import urlopen

transcripts = "http://spongebob.wikia.com/wiki/List_of_transcripts#Season"

rawHTML = urlopen(transcripts).read()

soup = BeautifulSoup(rawHTML, "html.parser")

links = []
for link in soup.find_all("table")[1].find_all("a"):
    links += ["http://spongebob.wikia.com/wiki/List_of_transcripts#Season" + link.get("href").strip()]
newlinks = [ link for link in links if u"(transcript)" in link ]
print(newlinks)
