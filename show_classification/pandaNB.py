#!/usr/bin/env python3

""" This script is a basis for show classification using the Pandas library
    5/23/18: This is currently predicting with MultinomialNB
"""

# Import libraries
import os
import pandas as pd
import numpy as np
import nltk

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer


# Open the transcripts
## Transcripts of interest are Southpark & SpongeBob
transcript_1 = "southpark_transcript.csv"
transcript_2 = "spongebob_transcript.csv"
## Go to the files
repo = os.path.split(os.getcwd())
script_folder = "temp"
path_1 = os.path.join(repo[0], script_folder, transcript_1)
path_2 = os.path.join(repo[0], script_folder, transcript_2)
## Load them using pd.read_csv
### South Park:
SP_df = pd.read_csv(path_1, header=0)#names=['season', 'episode', 'character', 'line'])
SP_df = SP_df.drop(columns=["Season", "Episode"])
SP_df['Show'] = 'South Park'
### SpongeBob:
SB_df = pd.read_csv(path_2, names=['Character', 'Line'])
SB_df['Show'] = 'SpongeBob'

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
    tr_shows = tr["Show"].values
    tst_lines = tst["Line"].values.astype('U')
    tst_shows = tst["Show"].values

    # Define the pipeline
    text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB())])
    ## TFIDF and CountVectorizer objects
    tfidf_transformer = TfidfTransformer()
    count_vect = CountVectorizer()

    # Now, we run Count Vec, TFIDF, and MultinomialNB
    X_train_counts = count_vect.fit_transform(tr_shows)
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    clf = MultinomialNB().fit(X_train_tfidf, tr_shows)
    text_clf = text_clf.fit(tr_lines, tr_shows)

    # Predict on the test lines
    predicted = text_clf.predict(tst_lines)
    tst_error = np.mean(predicted == tst_shows)
    return tst_correct


data = [SB_df, SP_df] # The data we will be using
tr, tst = train_test(data) # Train and test sets
score = show_pred(tr, tst) # The resulting error in classification

print(score) # Show the amount correct
