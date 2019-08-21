from urllib import request

import nltk

# access to electric books (txt)
url = 'http://www.gutenberg.org/files/2554/2554-0.txt'
response = request.urlopen(url)
raw = response.read().decode('utf-8')

tokens = nltk.word_tokenize(raw)  # nltk.text.Text

text = nltk.Text(tokens)
text.collocations()

raw.find('PART I')
raw.rfind('End of Project Gutenberg\'s Crime')