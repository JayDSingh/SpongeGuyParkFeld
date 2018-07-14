#simultaneously compiles all the transcript links from all seasons into a single list
#does not include Shorts (Shorts transcripts are formatted into multiple tables) and Rides (not actually part of the show) 

from bs4 import BeautifulSoup
from urllib.request import urlopen

transcripts = ["http://spongebob.wikia.com/wiki/List_of_transcripts#Season", 
               "http://spongebob.wikia.com/wiki/List_of_transcripts#2",
               "http://spongebob.wikia.com/wiki/List_of_transcripts#3",
               "http://spongebob.wikia.com/wiki/List_of_transcripts#4",
               "http://spongebob.wikia.com/wiki/List_of_transcripts#5",
               "http://spongebob.wikia.com/wiki/List_of_transcripts#6",
               "http://spongebob.wikia.com/wiki/List_of_transcripts#7",
               "http://spongebob.wikia.com/wiki/List_of_transcripts#8",
               "http://spongebob.wikia.com/wiki/List_of_transcripts#9",
               "http://spongebob.wikia.com/wiki/List_of_transcripts#10",
               "http://spongebob.wikia.com/wiki/List_of_transcripts#11",
               "http://spongebob.wikia.com/wiki/List_of_transcripts#Movies",
               "http://spongebob.wikia.com/wiki/List_of_transcripts#Specials",]

links = []
newlinks = []

for season in transcripts:
    rawHTML = urlopen(season).read()
    soup = BeautifulSoup(rawHTML, "html.parser")
    for link in soup.find_all("table")[1].find_all("a"):
        links += [season + link.get("href").strip()]
    newlinks += [ link for link in links if u"(transcript)" in link]

    
    
    
    
    
    
    
    
    
    #compiles all the transcript links from season 1 into a list (just a test)

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
