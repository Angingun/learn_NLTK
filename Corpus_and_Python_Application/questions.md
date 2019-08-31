
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Chapter 2](#chapter-2)

<!-- /code_chunk_output -->


# Chapter 2

```python
# p9
from nltk.book import * 
from nltk.corpus import inaugural
print(inaugural.fileids()) # print() needed
```

```python
#p21
from nltk.corpus import PlaintextCorpusReader 
corpus_root = r'C:\Users\acer\Desktop'
corpora = PlaintextCorpusReader(corpus_root, ['1.txt'])
corpora.fileids()
myfiles = corpora.words('1.txt')
print(len(set(myfiles))/len(myfiles)) # print() needed
```

```python
#p18: false commands
pip install python-docx #space removed 
```

```python 
#p19: improper grammar
doc2 = ' '.join(whole_text) #space needed
```

```python
# p21: python 3+
from __future__ import division #remove the line
```

```python
# p20: 
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'C:\Users\acer\Desktop'
corpora = PlaintextCorpusReader(corpus_root, ['1.txt'])
corpora.fileids() #redundant line
myfiles = corpora.words('1.txt')
print(len(set(myfiles))/len(myfiles)) # print needed
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

# Chapter 3

```python 
# p57
import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r"text"
corpora = PlaintextCorpusReader(corpus_root, ['1.txt'])
corpora.fileids()
myfiles = nltk.Text(corpora.words('1.txt')) 
print(len(myfiles), len(set(myfiles)), len(myfiles)/len(set(myfiles)))
```
**method & function in python:**
Method
1. Method is called by its name, but it is associated to an object (dependent).
2. A method is implicitly passed the object on which it is invoked.
3. It may or may not return any data.
4. A method can operate on the data (instance variables) that is contained by the corresponding class

Functions
1. Function is block of code that is also called by its name. (independent)
2. The function can have different parameters or may not have any at all. If any data (parameters) are passed, they are passed explicitly.
3. It may or may not return any data.
4. Function does not deal with Class and its instance concept.

Difference between method and function
1. Simply, function and method both look similar as they perform in almost similar way, but the key difference is the concept of **‘Class and its Object‘**.
2. Functions can be called **only by its name**, as it is defined independently. But methods **can’t be called by its name only**, we need to invoke the class by a reference of that class in which it is defined, i.e. method is defined within a class and hence they are dependent on that class.





