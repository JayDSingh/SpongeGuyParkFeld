# SpongeGuyParkFeld

# Current Progress Timeline


### 2/23/18

Seinfeld Team:

* Started to work on consolidating our code into one file (combinedcode.py).
* CSV file is no longer delimited by commas incorrectly. Previously each time a "," appeared in the script it would register as a new cell in the CSV file. Now, the commas no longer force a new cell to be created.
* The RegEx now matches for the entire \<p\> tag rather than just up to the colon (:)
* Going forward we want to format the CSV to include the episode number and perhaps season number. Also, removing the \<p\> tags and backslashes around commas.
* We will also want to remove scene directions which are either in brackets [] or percent signs %%
* There is also an issue where certain episodes are repeated twice. We don't know why this is occurring but it is something to work on next.
  
Spongebob Team:

* The sample python program is in progress in testScrape.py. The progress that is made will be updated in that file, and is explained there in more detail.

>* This is the first test scraper for the Spongebob scripts. 
>* What I have done: I have learned and accomplished how to get the script from 
>* the 1st episode by following the plan I previously laid out in the test 
>* folder. I have gotten all the lines with the tags into the variable called
>* lines. We can take the text out using .get_text(), but we want to retain
>* all the css tags so that it is easier to put the data into a csv file!
>* Working on how to put the lines into the csv file is the next step.

* Also analyzed code used by the Seinfeld Team for cleaning scripts and got familiar with HTML markers and regular expressions.
 
* TODO: Figure out how to format the data into a csv file in the desired format (Southpark is our reference).

### 2/15/18

Seinfeld Team:

* In the Seinfeld script pages, all the script data is stored in a \<div\> with the id "content". Within this all the actual script data is within \<p\> tags. We wish to begin our scraping at the first \<p\> tag with a character speaking. For example, a line that says "Jerry: hello world" rather than "Transcribed by: John Cena" nor "Cast:".
  
* In order to do this, we developed a Regular Expression that matches lines (\<p\> tags) wherein there is a colon and there is only one word before the colon, and there is non-null text after the colon.
  
```
  ^[^\s]*[\w]+[\s]*:(?=\s*\w)
 ```
 
* We have implemented this into a file called 'testing_soup.py' wherein we scrape the data in one of the seinfeld scripts and attempt to select only the correct \<p\> tags using the RegEx defined earlier.

* We have begun to attempt to create a program which instead of only scraping one script at a time, now goes through the list of script URLs generated in 'soup.py' and attempts to generate a well formatted CSV file that incorporates all the episodes and all relevant data (speaker, episode number, line text, episode date). The only thing excluded so far is stage data. This is in 'combinedcode.py'

* Going forward we want to consolidate everything together. The goal is to have one complete python program which can 1) pull all the episode script URLs & HTML docs, 2) generate BeautifulSoup objects from each of these, 3) extract out the relevant data (correct \<p\> tags within the 'content' \<div\>), and 4) create a well-formatted CSV file with this with clean data.

Spongebob Team:

* Repurposed seinfeld code in order to extract all URLs from spongebob page into a Python list. This allows us to systematically scrape each script.

* For each individual spongebob transcript page the script is in a \<ul\> tag. Every line of text is contained within a \<li\> tag within the \<ul\> tag. We will start scraping from the \<li\> tag which has the first character name in a bold (\<b\>) tag. This will allow us to get rid of extraneous data before the actual script starts. So for each transcript page the scraping starts at the first \<li\> tag with a \<b\> tag within it.

* Going forward, we will write a sample python program which extract all the script data line by line starting from the correct place. Then, we will try to generalize it to all the script pages using the 'urlscraping.py' file just as the seinfeld group is doing.

# Abstract
We will clean and analyze online transcripts of several popular American sitcoms (Family Guy, South Park, Seinfeld, Spongebob) and present our findings.
Our groups are looking to gain some insight onto the development of humor from more to less mature sitcoms as one of the primary goals in this project.
We also look to compare the complexity of vocabulary between the shows.
The desired outcome of this project is a text generator which will be able to create new content based on the styles of these individual shows.

# Contributors

Jason, Jay, Liam,  Evan, Jerry, Mikaela, Michelle, Euclid, Stevyn, and Lauren.  

# Timeline

We split this project into two main parts, with each group working independently.

## Part one
Weeks (2-5)

Two groups will scrape transcripts from the shows from the internet, clean the data, and make sure the data are in a useable format.  

## Part two
Weeks (6-10)

Once part one is completed, two groups (not necessarily the same members as previous two groups) will analyze the scraped data for sentiment and vocabulary complexity shifts.  Other focuses may arise as the project continues, but for now, those are the main goals.  

After analysis is completed, we hope to write a publication-quality article about our findings (in the Labyrinth).

# Steps to completing the project

1. Pick a standard format in which to store script data.
2. Write a program that goes to a web page and stores the script data in that standard format.
3. Look at the results of converting the data into that format.
4. Clean the data where necessary.
5. Write functions that take measurements/count specific phenomena in the data.
6. Produce data visualizations/report stats.
7. Perform an analysis on the numbers.
8. Write an article explaining analysis/summarizing the results.

# Important Python packages

[Beautiful soup](https://www.crummy.com/software/BeautifulSoup/)  
[Pandas](https://pandas.pydata.org/)  
[Nltk](http://www.nltk.org/) 

# Online Scripts

[Spongebob](http://spongebob.wikia.com/wiki/List_of_transcripts#Season)  
[South Park](https://www.kaggle.com/tovarischsukhov/southparklines)  
[Seinfeld](http://www.seinfeldscripts.com/)  

# Conclusion

We hope to learn something about the target audiences for each show based on the transcripts of those shows based on the vocabulary used and general tone of dialogue.  
