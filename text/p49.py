import nltk
from nltk.corpus import brown, PlaintextCorpusReader


corpora = PlaintextCorpusReader(r'C:\Users\\acer\Desktop\corpus _python\\text', ['1.txt'])
text = corpora.raw('1.txt')
tokens = nltk.word_tokenize(text)
brown_tagged_sents = brown.tagged_sents()
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
tagged_text = unigram_tagger.tag(tokens)
print(tagged_text)
