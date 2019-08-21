from bs4 import BeautifulSoup
from urllib import request

import nltk

#accessing html (BeautifulSoup)
url = 'http://news.bbc.co.uk/2/hi/health/2284783.stm'
html = request.urlopen(url).read().decode('utf-8')

raw = BeautifulSoup(html, 'html.parser').get_text()
tokens = nltk.word_tokenize(raw)

