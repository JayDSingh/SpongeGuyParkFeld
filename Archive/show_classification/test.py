import csv
import nltk
input_file = open("All-seasons.csv", "r")
for row in csv.reader(input_file):
    sentence = str(row)
    tokens = nltk.word_tokenize(sentence)
    print (tokens)
