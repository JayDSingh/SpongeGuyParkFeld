import pandas as pd
import numpy as np
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
import random
text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB())])
count_vect = CountVectorizer()
df = pd.read_csv("All-seasons.csv", names=['season', 'episode', 'character', 'line'])
dfd = df[['character', 'line']]
dfd['show'] = 'SP'
pf = pd.read_csv("bigcsv1.csv", names=['character', 'line'])
pf['show'] = 'SS'
frames = [dfd, pf]
result = pd.concat(frames)
result1 = result.sample(frac=1)
tfidf_transformer = TfidfTransformer()
result1.index = range(result1.shape[0])
R = result1.loc[:90000,:]
S = result1.loc[90000:,:]
L = R['line']
X_train_counts = count_vect.fit_transform(L)
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
P = R['show']
clf = MultinomialNB().fit(X_train_tfidf, P)
T = S['line']
J = S['show']
text_clf = text_clf.fit(L, P)
predicted = []
predicted = text_clf.predict(T)
print(np.mean(predicted == J))
