# Current Progress Timeline

### 5/28/18
Implemented Random Forests in [main/pandaRF.py](main/pandaRF.py). Achieved 88.4% accuracy.

### 5/27/18
There are now README.md files in [main](main) and [temp](temp). From now on we should put the working files which are needed to run the project in [main](main) and things that are not essential or need more work in [temp](temp). Also update the README.md files in both to explain what each file does.

[PandaNB.py now works with all three shows and has been moved to the main directory](main/PandaNB.py). It achieves 75.8% accuracy clasifying between the three shows.

##### Moving forward
At this point we should try some new algorithms besides Naive Bayes. We may also try to update and integrate in `stemmingpredict.py`, `gridsearchparams.py` and other files to further improve our model. As of now it still uses things like 'bigcsv' so they are being moved to temp.

### 5/24/18

##### Seinfeld Transcript is now ready-to-go.
I believe it is totally complete however I may have missed something so feel free to check it.


`PandasNB.py` is now working & properly annotated
Checklist for the meeting tonight:
* Exploratory data analysis on the data sets
* Try different ML methods on `PandasNB.py`
* add cross validation to pandaNB.py
* find best k-folds for cross validation

#### Got word2vec algorithm working on SpongeBob & South Park.
Currently, the code plots a similarity graph for SpongeBob.

Results:
* A word similarity graph. Can easily be modified to show South Park
* First Neural Net in our analysis.
Next Step:
Use weights of words found by NN to do unsupervised learning & clustering.

### 5/22/18

##### Seinfeld
Discovered that the second re.sub deletes everything enclosed in brackets up until the next colon. (i.e. "SpongeGuyParkFeld \[hello] yes: after the colon:" --> "SpongeGuyParkFeld after the colon"

See main/seinfeld_transcript.csv file for more details.

### 5/19/18

##### Seinfeld
Speaker and line are now separated however every place where there is a colon (:) is being treated as a new entry. Many of the 'lines' have colons (:) within them and that is causing a lot more entries whereas they should all be combined (outside of the speaker).

See main/seinfeld_transcript.csv file for more details.

Also, clean_seinfeld.py may become unnecessary as the cleaning is being done in scrape_seinfeld.py

#### General

* Get Naive Bayes to work with Pandas in pandaNB.py in show_classification
* Explore alternative model classification algorithms other than Naive Bayes
* Explore alternative model accuracy evaluation metrics

### 5/1/18

##### Spongebob

`Clean_bigcsv.py` is up, which cleans the mergedbigcsv.csv. The goal here is to have a list of lines per character.
Also, it seems like NBpredict.py is successful in getting an 80% classification rate on the Spongebob & Southpark datasets.

* Looking ahead, we should try to implement some unsupervised learning, i.e. http://www.aclweb.org/anthology/C00-1066 or https://tech.smartling.com/text-categorization-the-hackathon-project-b8c33ae94c24.

### 4/26/18

For the Machine Learning portion of the project, we are drawing heavily from the following article: https://towardsdatascience.com/machine-learning-nlp-text-classification-using-scikit-learn-python-and-nltk-c52b92a7c73a

##### Seinfeld cleaning

* Episodes 4, 10, and 11 (among others) are missing (confirm this). For episode 4 we figured out that the reason is that all of the script \<p\> tags have the form \<p align="left">Broadcasted: June 14, 1990 for the first time.\</p\> which does not work with our regex of ^[^\s]*[\w]+[\s]*:.+

* So all the \<p\> tags for this episode (and likely more) are not be included in the CSV. We still are unsure why other episodes such as 10 and 11 are being excluded since they have normal \<p\> tags.

* Also, in all of the rows, lines that were totally enclosed in angle brackets "[]" were being removed but not lines that had angle-bracketed sections as only a part of them. We are in the process of writing code to remove any instances of bracketed text.

### 4/22/18

In the past few meetings we began looking towards the analysis portion of our project. Our first project is to predict which show a given line of text comes from. We have begun to read in and tokenize the south park script data into NLTK (in /showclassification/test.py) and will soon add the spongebob and seinfeld data.

We also tried an alternative method of reading in the south park script data using Pandas (in /teamliam/SouthParkDict.py).

The spongebob data is almost clean we simply need to slightly reformat the data. Some of the lines are split across multiple columns whereas they should all be in one column (as in the south park data).

* So we will write a python script which takes the CSV and then appends all columns beyond 'B' (from C onwards) onto the 'B' column.

The seinfeld data is still incomplete but we will only return to perfect it if we have more time. Until then we will use what we have. We will

* Remove stage directions or things in "[]" angle brackets
* Remove lines starting with "cast:" or "broadcast:"
* Separate out the character names so that we can remove them.
* If doable with limited time we will fix the issue where episodes are not included.

* in teamjay/temp.py, there is the start of splitting speaker/line into key : value pairs.  The function should work, but reading the csv correctly does not.  

### 3/2/18

Everyone started working in virtuall environments and created 'requirements.txt' files.

Seinfeld Team: 

* Fixed encoding issue for PCs in combinedcode.py.

#### Current issues:

* Missing 78 episodes out of 180 total.  70 of which are completely blank.  

* Brackets (ie stage directions) are not all being removed, though they should.  

* Including things like "Cast:", "Broadcasted:".  

* We still do not know why some episodes are missing.

* Some <p> tags are being excluded because they do not start with "Name: _____" even though we want them. We also seem to be missing speakers with multiple words in name, ie "Soup Nazi:" or "Jerry and Elaine:". We will want to find a way to get all of the <p> tags we want so as to not exclude any data.

Spongebob Team:

* Wrote functions to separate the speaker and dialogue from each line (segment_line() in test_scrape.py)

* Next steps: Test which episodes we can read with BS

* Segment each line with episode # and season # and add to csv file



* /teamliam/Temp-/test_csv.py is beginning to generate a csv. However problems are that it is in the incorrect format. We want separate 'name' and 'line' columns but they are still together in a single column. Using the code from testScrape.py (which separates speaker 'name' and dialogue 'line') we should hope to solve this. However, this still needs to be done.

### 2/26/18

Seinfeld Team:

* Continued to work on combinedcode.py.  

* Cleaned \<p\> tags (opening and closing) and the bracketed stage directions from the csv with regex.  

* Fixed the issue of not getting multi-line scripts.

#### Current issues:

* Can't loop through links and open them

#### Current issues:

* Some episodes are not getting scraped (4, 8, 10, 14 \[two spaces after colons?], 23 \[no colons after names], 32, and possibly more).  

* \x92 or ```&#146;``` or right quotation mark are breaking code for PC.  

```
Traceback (most recent call last):
  File "C:/Users/Lauren Shin/Documents/github/SpongeGuyParkFeld/teamjay/combinedcode.py", line 67, in <module>
    filewriter.writerow(matches)
  File "C:\Users\Lauren Shin\AppData\Local\Programs\Python\Python36\lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode character '\x92' in position 143: character maps to <undefined>
```
* The two-part finale is on one page, and both the first and second finale links link to that page.  The first finale script is scraped twice while the second is not scraped at all.  

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
