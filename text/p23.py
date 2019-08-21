from nltk.corpus import PlaintextCorpusReader
corpus_root = r'text'
corpora = PlaintextCorpusReader(corpus_root, ['1.txt'])
#corpora.fileids()
myfiles = corpora.words('1.txt')
len(set(myfiles))/len(myfiles)

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from nltk import ngrams
n = 3
x = [word.lower() for word in myfiles if word.isalpha()]
n_grams = ngrams(x, n)
log = open(r"text/3.txt", 'w')
for grams in n_grams:
    if len(set(grams) & set(stop_words)) == 0:
        #print(grams)
        log.write(str(grams) + '\n')     
log.close()
