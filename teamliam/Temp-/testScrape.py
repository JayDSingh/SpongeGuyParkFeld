#Author: Jerry Liu
#Today is February 23, 2018.
#This is the first test scraper for the Spongebob scripts. 
#What I have done: I have learned and accomplished how to get the script from 
#the 1st episode by following the plan I previously laid out in the test 
#folder. I have gotten all the lines with the tags into the variable called
#lines. We can take the text out using .get_text(), but we want to retain
#all the css tags so that it is easier to put the data into a csv file!
#Working on how to put the lines into the csv file is the next step.


from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import re
import pandas as pd

#type(html_soup)
#bs4.BeautifulSoup

firstEpi = "http://spongebob.wikia.com/wiki/Help_Wanted_(transcript)"
firstHTML = urlopen(firstEpi).read()

html_soup = BeautifulSoup(firstHTML,'html.parser')

#find the <ul> content, aka the actual script
content = html_soup.find('ul', attrs={'class': None})

#find each bullet
lines = content.findAll('li')

lineList = []

for x in lines:
	lineList.append(re.sub("[\(\[].*?[\)\]]", "", x.getText()))

#print(lineList)

#csv.register_dialect('colon', delimiter=':')

# take the character names
def get_character(line):
    x = re.search("^[^:]*:*", line) # and not followed by another :?
    y = x.group(0)
    y = re.sub(":", "", y)
    return y

# take the dialogue
def get_dialogue(line):
    x = re.search(":+.*", line)
    y = x.group(0)
    y = re.sub("^[^:]*:\s*", "", y)
    return y

with open('testline.csv', 'w', newline='', encoding = 'utf-8') as csvfile:
    testwriter = csv.writer(csvfile, delimiter='\n',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    testwriter.writerow(['Season 1', 'Ep 1'])

    for y in lineList: #for the strings in this list, which are in char: dialogue format
    	charAndLine = y.split(":") #is an array with char and line separated
    	character = charAndLine[0] #they have have a character
    	if len(charAndLine) == 2: #not all chars have dialogue (due to cleaning of actions)
    		dialogue = charAndLine[1]
    		testwriter.writerow([character, dialogue])
    		#next step is to use pandas to make this into the desired format
    		#right now every other row is the same thing
    		#ie every other row is either a character or a line
    		#so we want to use pandas to format into a nice table!

#print(html_soup.prettify())

#for x in lines:
	#print(x.getText())

#print(lines)
