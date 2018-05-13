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
for joup in soup.find_all("table"):
    pinks = joup.find_all("a")
    for pink in pinks:
    # strips string of whitespace (some have intitial spaces)
    # and concatenates it with homepage url to form the full url
    # adds it to the list of links
        links += ["http://spongebob.wikia.com" + pink.get("href").strip()]

for i in range(868,len(links)):
    links.pop()

linksrem = []
for i in range(867):
    if i%2 == 1:
        linksrem.append(links[i])

J = []
for link in linksrem:

    firstHTML = urlopen(link).read()
    html_soup = BeautifulSoup(firstHTML, 'html.parser')

    # find the <ul> content, aka the actual script
    content = html_soup.find('ul', attrs={'class': None})

    # find each bullet
    lines = content.findAll('li')

    P = []
    for x in lines:
        P.append(re.sub("[\(\[].*?[\)\]]", "", x.getText()))

    L = []
    for i in P:
        L.append(str(i))

    M = []
    for line in L:
        m = line.strip('\n')
        M.append(m)

    for line in M:
        J.append(line.split(':'))


with open('temp_spongebob_transcript.csv', 'w', newline='', encoding='utf-8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for line in J:
            spamwriter.writerow(line)


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
