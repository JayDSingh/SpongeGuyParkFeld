# read in every episode of seinfeld script to csv file

# attempt at grabbing all the urls for seinfeld scripts
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

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
	filewriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	filewriter.writerow(['Season Episode Character Dialogue'])
	for single_link in links:
		# soup_tester.py
		# url to look at
		firstEpi = single_link
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

		contentdiv = stew.find("div", {"id": "content"})
		paragraphs = contentdiv.find_all("p")

		filewriter.writerow(paragraphs)


