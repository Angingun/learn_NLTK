
The book is based on python 2.6 and written in jupyter notebook


```python
# p21: python 3+
from __future__ import division #remove the line
```

```python
# p23
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from nltk import ngrams
n = 3
x = [word.lower() for word in myfiles if word.isalpha()]
n_grams = ngrams(x, n)
log = open(r"text/3.txt", 'w')
for grams in n_grams:
    if len(set(grams) & set(stop_words)) == 0:
#        print >>log, grams 
         log.write(str(grams) + '\n') # what is "print >>"
log.close()
```

```python
# p35, etc
corpora = PlaintextCorpusReader(corpus_root, ['total book1.txt'])
corpora.fileids() # redundant line
myfiles = corpora.words('total book1.txt')
```









