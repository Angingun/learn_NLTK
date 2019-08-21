import nltk
text = "Springer Handbook provides a concise compilation of approved key information on methods of research, general principles, and functional relationships in physical and applied sciences."
text1 = nltk.word_tokenize(text)
fdist = nltk.FreqDist(text1)
fdist['of']
fdist.freq('of')
fdist.N()
fdist.items()
fdist.plot()
fdist.most_common(2)
fdist.hapaxes()