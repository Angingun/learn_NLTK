from nltk.book import *

# count
len(text3)

sorted(set(text3))
len(set(text3))
len(set(text3)) / len(text3)
lexical_diversity = lambda text: len(set(text)) / len(text)

text3.count('smote')
100 * text4.count('a') / len(text4)
per = lambda count, total: 100 * count / total