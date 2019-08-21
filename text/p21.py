from nltk.corpus import PlaintextCorpusReader
corpus_root = r'C:\Users\acer\Desktop'
corpora = PlaintextCorpusReader(corpus_root, ['1.txt'])
#corpora.fileids()
myfiles = corpora.words('1.txt')
len(set(myfiles))/len(myfiles)