import csv
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB())])
count_vect = CountVectorizer()
input_file = open("All-seasons.csv", "r", encoding="utf8")
L = []
T = []
J = []
acc = 0
for row in csv.reader(input_file):
    if acc < 60000:
        L.append(str(row[3]))
        acc += 1
    if acc == 60000:
        T.append(str(row[3]))
        J.append('SP')




input_file1 = open("bigcsv1.csv", "r", encoding="utf8")
bacc = 0
for row in csv.reader(input_file1):
    if bacc < 40000:
        L.append(str(row[1]))
        bacc += 1
    if bacc == 40000:
        T.append(str(row[1]))
        J.append('SS')


P = []
X_train_counts = count_vect.fit_transform(L)
for i in range(0,60000):
    P.append('SP')
for i in range(0,40000):
    P.append('SS')
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
clf = MultinomialNB().fit(X_train_tfidf, P)
text_clf = text_clf.fit(L, P)
predicted = []
predicted = text_clf.predict(T)
print(np.mean(predicted == J))
