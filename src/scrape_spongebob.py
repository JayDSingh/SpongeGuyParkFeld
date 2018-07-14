#import libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import re
# url to look at
transcripts = "http://spongebob.wikia.com/wiki/List_of_transcripts#Season"
# opens url and reads html contents
rawHTML = urlopen(transcripts).read()

# makes beautiful soup object and parses html from opened url
soup = BeautifulSoup(rawHTML, "html.parser")

links = []

#looks through each 'a' tag in the second table in the webpage
for table in soup.find_all("table"):
    names = table.find_all("a")
    for name in names:
    # strips string of whitespace (some have intitial spaces)
    # and concatenates it with homepage url to form the full url
    # adds it to the list of links
        links += ["http://spongebob.wikia.com" + pink.get("href").strip()]

#we end up with more than just the links so we need to remove that part of the list
for i in range(868,len(links)):
    links.pop()
#we ended up with double the links so we need to get half of them, each duplicate comes directly after the first
linksnew = []
for i in range(867):
    if i%2 == 1:
        linksnew.append(links[i])
#create empty list
J = []
for link in linksnew:
    #open HTML file
    firstHTML = urlopen(link).read()
    #create beautiful soup object
    html_soup = BeautifulSoup(firstHTML, 'html.parser')

    # find the <ul> content, aka the actual script
    content = html_soup.find('ul', attrs={'class': None})

    # find each bullet
    lines = content.findAll('li')
    #create an empty list to store cleaned lines
    P = []
    for x in lines:
        P.append(re.sub("[\(\[].*?[\)\]]", "", x.getText()))
    #create an empty list to store cleaned lines from P as strings
    L = []
    for i in P:
        L.append(str(i))
    #create empty list to hold lines after removing new line characters
    M = []
    for line in L:
        m = line.strip('\n')
        M.append(m)
    #split each element of M into a list of character and line, and add it to J
    for line in M:
        J.append(line.split(':'))

#create temporary SpongeBob transcript file
with open('temp_spongebob_transcript.csv', 'w', newline='', encoding='utf-8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for line in J:
            spamwriter.writerow(line)

#go into the temporary SpongeBob file and put any parts of lines that are past the 2nd column into the 2nd column in the new SpongeBob file
input_file = open("temp_spongebob_transcript.csv", "r", encoding="utf8")
with open('spongebob_transcript.csv', 'w', newline='', encoding='utf-8') as csvfile:
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
