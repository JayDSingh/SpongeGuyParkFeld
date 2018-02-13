# General Workflow

## 1st Checkpoint (2/12):
### Web scraping
Scrape the Spongebob and Seinfeld data, and be able to store as csv in a desired standard format, so that we can write functions that work for all three data sets of SpongeBob, Seinfeld, and South Park.  
Since the South Park data is cleaned, we should use that csv file as a guide.  
It has the layout:  
  
10,1,Stan,"You guys, you guys! Chef is going away.  
"  
for each line.

### Humor classification
Lets put the mountain of contextual data to work and do some data mining on humor.
We manually add a response variable indicating that a line is part of a joke.  
  Could use indicator = humor or not humor, or look for jokes of the form:  
    1. Setup - A future event suddenly has meaning  
    2. Reinforcement - The "build-up" of the joke  
    3. Payoff, i.e. punchline  
  +: Gives another response to work with  
    Possibly interesting results with a joke generator  
  -: May be clunky if a joke is 1 or 2 lines, or situational  
    Requires manual input  

## 2nd Checkpoint (2/19):
Think of measurements to take and write code to obtain statistics and establish an analysis based on these measurements.  
Goals:  
  *Have all the seasons (clean?).
  *Begin classifying Seinfeld and Spongebob
  *Plot some basic metrics (word freq, character line freq)

## 3rd Checkpoint(2/26):
Run the code on the data and obtain measurements, then look at the results.  
Make a visibly intuitive 

## Final task:
Report the most interesting and accurate conclusions to be drawn from the data in an article in The Labyrinth. 
