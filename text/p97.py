import nltk
from nltk.corpus import stopwords
from nltk import FreqDist
text = """
       Springer Handbook provides a concise compilation of approved key information on methods of research, general principles, and functional relationships in physical and applied sciences.The world’s leading experts in the fields of physics and engineering will be assigned by one or several renowned editors to write the chapters comprising each volume. The content is selected by these experts from Springer sources (books, journals, online content) and other systematic and approved recent publications of scientific and technical information. This handbook contains 3 volumes.
       """
stop_words = nltk.corpus.stopwords.words('english')
x = [word.lower for word in text.split() if word.isalpha()]
y = [word for word in x if word not in stop_words]
FreqDist(y)  # no results ???