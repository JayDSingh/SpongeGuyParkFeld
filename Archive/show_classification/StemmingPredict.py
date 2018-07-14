#import the libraries we need
import csv
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
from nltk.stem.snowball import SnowballStemmer
#pipeline our functions to make them easier to call
text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB())])
count_vect = CountVectorizer()
input_file = open("southpark_transcript.csv", "r", encoding="utf8")
tr_lines = []
tr_targets = []
tst_lines = []
tst_targets = []
acc = 0 #accumulator
for row in csv.reader(input_file):
    if acc < 60000:
        tr_lines.append(str(row[3]))
        acc += 1
    if acc == 60000:
        tst_lines.append(str(row[3]))
        tst_targets.append('SP')

input_file1 = open("bigcsv1.csv", "r", encoding="utf8")
bacc = 0 #new accumulator
for row in csv.reader(input_file1):
    if bacc < 40000:
        tr_lines.append(str(row[1]))
        bacc += 1
    if bacc == 40000:
        tst_lines.append(str(row[1]))
        tst_targets.append('SS')

for i in range(0,60000):
    tr_targets.append('SP')
for i in range(0,40000):
    tr_targets.append('SS')

X_train_counts = count_vect.fit_transform(tr_lines)
stemmer = SnowballStemmer("english", ignore_stopwords=True)
class StemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(StemmedCountVectorizer, self).build_analyzer()
        return lambda doc: ([stemmer.stem(w) for w in analyzer(doc)])
stemmed_count_vect = StemmedCountVectorizer(stop_words='english')
text_mnb_stemmed = Pipeline([('vect', stemmed_count_vect),('tfidf', TfidfTransformer()),('mnb', MultinomialNB(fit_prior=False))])
text_mnb_stemmed = text_mnb_stemmed.fit(tr_lines, tr_targets)
predicted_mnb_stemmed = text_mnb_stemmed.predict(tst_lines)
print(np.mean(predicted_mnb_stemmed == tst_targets))
