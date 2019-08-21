import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r"text"
corpora = PlaintextCorpusReader(corpus_root, ['1.txt'])
corpora.fileids()
myfiles = nltk.Text(corpora.words('1.txt'))
print(len(myfiles), len(set(myfiles)), len(myfiles)/len(set(myfiles)))
