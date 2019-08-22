
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [NLP](#nlp)
- [chapter 1: Language Processing and Python](#chapter-1-language-processing-and-python)
- [chapter 2:](#chapter-2)
- [chapter 3: Processing Raw Text](#chapter-3-processing-raw-text)

<!-- /code_chunk_output -->

# NLP

NLP, Natural Language Processing, involves "understanding" complete human utterances, at least to the extent of being able to give useful responses to them.

# chapter 1: Language Processing and Python
```python
from nltk.book import *

# search text
text1.concordance('Monstrous')  # text1 is an instance of 'nltk.text.Text'
text1.similar('Monstrous')  # other words appear in the similar range of contest
text1.common_contexts(['monstrous', 'very']) # examine just the contexts that are shared by two or more words

text4.dispersion_plot(
    ['citizens', 'democracy', 'freedom', 'duties', 'America'])

```

![Image of dispersion_plot](https://github.com/Angingun/learn_NLTK/blob/master/NLTKofficials/basics/dis_plot.png)
```python
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

```

```python
from nltk.book import *

# Frequency distribution
from nltk.probability import FreqDist
fdist1 = FreqDist(text1)  # fdist1 is an instance of FreqDist class
print(fdist1)  # FreqDist.__str__
fdist1.most_common(50)
fdist1['whale']

fdist1.plot(50, cumulative=True)  # generate a cumulative frequency plot

# Functions Defined for NLTK's Frequency Distributions or methods set in FreqDist class
fdist = FreqDist(samples) 	# create a frequency distribution containing the given samples
fdist[sample] += 1 	# increment the count for this sample
fdist['monstrous'] 	# count of the number of times a given sample occurred
fdist.freq('monstrous') 	# frequency of a given sample
fdist.N() 	# total number of samples
fdist.most_common(n) 	# the n most common samples and their frequencies
for sample in fdist: 	# iterate over the samples
fdist.max() 	# sample with the greatest count
fdist.tabulate() 	# tabulate the frequency distribution
fdist.plot() 	# graphical plot of the frequency distribution
fdist.plot(cumulative=True) 	# cumulative plot of the frequency distribution
fdist1 |= fdist2 	# update fdist1 with counts from fdist2
fdist1 < fdist2 	# test if samples in fdist1 occur less frequently than in fdist2

```
![cumu_freq](https://github.com/Angingun/learn_NLTK/blob/master/NLTKofficials/basics/cumu_freq.png)

```python
from nltk.book import *
from nltk.probability import FreqDist

# Fine-grained selection of words
v = set(text1)
long_words = [w for w in v if len(w) > 15]  # generator 
sorted(long_words)
""" 
['CIRCUMNAVIGATION', 'Physiognomically', 'apprehensiveness', 'cannibalistically',
'characteristically', 'circumnavigating', 'circumnavigation', 'circumnavigations',
'comprehensiveness', 'hermaphroditical', 'indiscriminately', 'indispensableness',
'irresistibleness', 'physiognomically', 'preternaturalness', 'responsibilities',
'simultaneousness', 'subterraneousness', 'supernaturalness', 'superstitiousness',
'uncomfortableness', 'uncompromisedness', 'undiscriminating', 'uninterpenetratingly']
  """

fdist5 = FreqDist(text5)
sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)
""" 
['#14-19teens', '#talkcity_adults', '((((((((((', '........', 'Question',
'actually', 'anything', 'computer', 'cute.-ass', 'everyone', 'football',
'innocent', 'listening', 'remember', 'seriously', 'something', 'together',
'tomorrow', 'watching']
  """
# collocations
text4.collocations()
"""
United States; fellow citizens; four years; years ago; Federal
Government; General Government; American people; Vice President; Old
World; Almighty God; Fellow citizens; Chief Magistrate; Chief Justice;
God bless; every citizen; Indian tribes; public debt; one another;
foreign nations; political parties
"""

```

```python
# Conditionals

sent7 = [
    'Pierre', 'Vinken', ',', '61', 'years', 'old', ',', 'will', 'join', 'the',
    'board', 'as', 'a', 'nonexecutive', 'director', 'Nov.', '29', '.'
]
[w for w in sent7
       if len(w) < 4]  # [',', '61', 'old', ',', 'the', 'as', 'a', '29', '.']


# Some Word Comparison Operators

s.startswith(t)  # test if s starts with t
s.endswith(t)  # test if s ends with t
t in s  # test if t is a substring of s
s.islower()  # test if s contains cased characters and all are lowercase
s.isupper()  # test if s contains cased characters and all are uppercase
s.isalpha()  # test if s is non-empty and all characters in s are alphabetic
s.isalnum()  # test if s is non-empty and all characters in s are alphanumeric
s.isdigit()  # test if s is non-empty and all characters in s are digits
s.istitle(
)  # test if s contains cased characters and is titlecased (i.e. all words in s have initial capitals)

```
# chapter 2: 





# chapter 3: Processing Raw Text

```python
from urllib import request

import nltk

# access to electric books (txt)
url = 'http://www.gutenberg.org/files/2554/2554-0.txt'
response = request.urlopen(url)
raw = response.read().decode('utf-8')

tokens = nltk.word_tokenize(raw)

text = nltk.Text(tokens)
text.collocations()

raw.find('PART I')
raw.rfind('End of Project Gutenberg\'s Crime')
```
