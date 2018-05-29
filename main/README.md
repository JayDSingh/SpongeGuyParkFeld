# Summary of Files

### `scrape_spongebob.py`
Generates `spongebob_transcript.csv`

Requires: *Nothing*


### `scrape_seinfeld.py`
Generates `seinfeld_transcript.csv` and superfluous `temp_seinfeld_transcript.csv`

Requires: *Nothing*

### `pandaNB.py`
Classifies between the three shows using Multinomial Naive Bayes. Achieves 75.8% accuracy.

Requires: `spongebob_transcript.csv` , `seinfeld_transcript.csv` , `southpark_transcript.csv`

### `csv processing.R`
Generates csv with the six more frequent speakers.  

Requires: R and dplyr, `spongebob_transcript.csv` , `seinfeld_transcript.csv` , `southpark_transcript.csv`
