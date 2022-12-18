from pandas import *

#Script to get word count from list of sentences from
# Turkish Sentence Dataset: https://www.kaggle.com/datasets/mahdinamidamirchi/turkish-sentences-dataset .

#reads sentences into list from text file.

with open("wiki.tr.txt", "r") as turkish_sentences:
    lines = turkish_sentences.readlines()
    line_strip = [line.rstrip() for line in lines]
    print(line_strip)

# Counts words

def word_count(string):
    res = len(string.split())
    return res

#Makes new data frame from list, with column name 'Sentence', and applies word count to create
# second column; 'Word Count'.

df = DataFrame(line_strip, columns = ['Sentence'])
print(df.head())
df['Word Count'] = df['Sentence'].apply(word_count)

print(df.head())





