import csv
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
from sklearn.model_selection import GridSearchCV
text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB())])
parameters = {'vect__ngram_range': [(1, 1), (1, 2)],'tfidf__use_idf': (True, False),'clf__alpha': (1e-2, 1e-3)}
count_vect = CountVectorizer()
input_file = open("All-seasons.csv", "r", encoding="utf8") #open the South Park csv
L = [] #list of lines for training data
T = []  #list of lines for test data
J = []  #list of tags for test data
acc = 0 #counter variable
for row in csv.reader(input_file):
    if acc < 60000:
        L.append(str(row[3]))
        acc += 1
    if acc == 60000:
        T.append(str(row[3]))
        J.append('SP')




input_file1 = open("bigcsv1.csv", "r", encoding="utf8") #open the SpongeBob csv
acc1 = 0 #new counter variable
for row in csv.reader(input_file1):
    if acc1 < 40000:
        L.append(str(row[1]))
        acc1 += 1
    if acc1 == 40000:
        T.append(str(row[1]))
        J.append('SS')


P = [] #training data tags
X_train_counts = count_vect.fit_transform(L)
for i in range(0,60000):
    P.append('SP')
for i in range(0,40000):
    P.append('SS')
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
clf = MultinomialNB().fit(X_train_tfidf, P)
text_clf = text_clf.fit(L, P)
predicted = [] #empty list
predicted = text_clf.predict(T) #list of predicted values for the test tags
gs_clf = GridSearchCV(text_clf, parameters, n_jobs=-1)
gs_clf = gs_clf.fit(L, P)
print(gs_clf.best_score_)
print(gs_clf.best_params_)
