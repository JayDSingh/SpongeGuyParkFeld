# Import libraries
import os
import pandas as pd
import numpy as np
import nltk

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer


# Open the transcripts
## Transcripts of interest are Southpark & SpongeBob
transcript_1 = "southpark_transcript.csv"
transcript_2 = "spongebob_transcript.csv"
transcript_3 = "seinfeld_transcript.csv"
## Go to the files
repo = os.path.split(os.getcwd())
script_folder = "data"
path_1 = os.path.join(repo[0], script_folder, transcript_1)
path_2 = os.path.join(repo[0], script_folder, transcript_2)
path_3 = os.path.join(repo[0], script_folder, transcript_3)

## Load them using pd.read_csv
### South Park:
SP_df = pd.read_csv(path_1, header = 0)#names=['season', 'episode', 'character', 'line'])
SP_df = SP_df.drop(columns=["Season", "Episode"])
SP_df['Show'] = 'South Park'
### SpongeBob:
SB_df = pd.read_csv(path_2, names=['Character', 'Line'])
SB_df['Show'] = 'SpongeBob'

### Seinfeld:
SF_df = pd.read_csv(path_3, header = 0)
SF_df['Show'] = 'Seinfeld'
SP_df = SP_df[SP_df['Character'] == 'Cartman' or 'Kyle' or 'Stan' or 'Butters' or 'Randy']
SB_df = SB_df[SB_df['Character'] == 'SpongeBob' or 'Patrick' or 'Sandy' or 'Mr. Krabs' or 'Squidward' or 'Plankton']
SF_df = SF_df[SF_df['Character'] == 'Jerry' or 'George' or 'Elaine' or 'Kramer']

# Separate the data into training and test sets.
# This is where CV goes.
def train_test(data): # input data as a list of pd.Dataframes
## Concatinate
    df = pd.concat(data)
    ## Shuffle the training data
    tr = df.sample(frac=0.8).reset_index(drop=True)
    ## Test data is the remainder in the original data
    tst = pd.merge(df, tr, how='outer', indicator=False)
    ## Shuffle the test data
    tst = tst.sample(frac=1).reset_index(drop=True)
    return tr, tst

# Now we will perform prediction
def show_pred(tr, tst):
    # Separate the lines and characters from the train & test sets
    tr_lines = tr["Line"].values.astype('U')
    tr_chars = tr["Character"].values
    tst_lines = tst["Line"].values.astype('U')
    tst_chars = tst["Character"].values

    # Define the pipeline
    text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', RandomForestClassifier())])
    ## TFIDF and CountVectorizer objects
    tfidf_transformer = TfidfTransformer()
    count_vect = CountVectorizer()

    # Now, we run Count Vec, TFIDF, and RandomForestClassifier

    text_clf = text_clf.fit(tr_lines, tr_chars)

    # Predict on the test lines
    predicted = text_clf.predict(tst_lines)
    tst_correct = np.mean(predicted == tst_chars)
    return tst_correct


data = [SB_df, SP_df, SF_df] # The data we will be using
tr, tst = train_test(data) # Train and test sets
score = show_pred(tr, tst) # The resulting error in classification

print(score) # Show the amount correct
