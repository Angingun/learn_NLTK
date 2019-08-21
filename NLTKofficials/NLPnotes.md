
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

@import "basics\search_text.py"
@import "basics\dis_plot.png"
@import "basics\count_.py"
@import "basics\frequency_distribution.py"
@import "basics\cumu_freq.png"
@import "basics\fine_grained_selection_of_words.py"
@import "basics\conditionals.py"

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
