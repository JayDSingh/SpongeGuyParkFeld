import csv
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
from sklearn.linear_model import SGDClassifier
text_clf_svm = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf-svm', SGDClassifier(loss='hinge', penalty='l2',alpha=1.5e-3, n_iter=30, random_state=100)),])
count_vect = CountVectorizer()
L = []
T = []
J = []
P = []
input_file1 = open("bigcsv1.csv", "r", encoding="utf8")
bacc = 0
for row in csv.reader(input_file1):
    if bacc < 30000:
        if str(row[0]) == 'SpongeBob':
            L.append(str(row[1]))
            P.append(str(row[0]))
            bacc += 1
        if str(row[0]) == 'Squidward':
            L.append(str(row[1]))
            P.append(str(row[0]))
            bacc += 1
        if str(row[0]) == 'Patrick':
            L.append(str(row[1]))
            P.append(str(row[0]))
            bacc += 1
        if str(row[0]) == 'Sandy':
            L.append(str(row[1]))
            P.append(str(row[0]))
            bacc += 1
        if str(row[0]) == 'Plankton':
            L.append(str(row[1]))
            P.append(str(row[0]))
            bacc += 1
        if str(row[0]) == 'Patrick':
            L.append(str(row[1]))
            P.append(str(row[0]))
            bacc += 1
    if bacc == 30000:
        if str(row[0]) == 'SpongeBob':
            T.append(str(row[1]))
            J.append(str(row[0]))
        if str(row[0]) == 'Squidward':
            T.append(str(row[1]))
            J.append(str(row[0]))
        if str(row[0]) == 'Patrick':
            T.append(str(row[1]))
            J.append(str(row[0]))
        if str(row[0]) == 'Sandy':
            T.append(str(row[1]))
            J.append(str(row[0]))
        if str(row[0]) == 'Plankton':
            T.append(str(row[1]))
            J.append(str(row[0]))
        if str(row[0]) == 'Patrick':
            T.append(str(row[1]))
            J.append(str(row[0]))


X_train_counts = count_vect.fit_transform(L)
_ = text_clf_svm.fit(L, P)
predicted_svm = text_clf_svm.predict(T)
print(np.mean(predicted_svm == J))
