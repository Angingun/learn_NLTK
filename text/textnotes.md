# read docx, p9
```python
import docx
import nltk
whole_text = []
doc1 = docx.Document(ur'C:/Users/acer/Desktop/python_test.docx')
paras = doc1.paragraphs
for p in paras:
    whole_context.append(p)
doc2 = ''.join(whole_context)
doc3 = doc2.split()
doc4 = nltk.Text(doc3)
doc4.concordance('by')
```

# read txt file, p21
```python
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'C:\Users\acer\Desktop'
corpora = PlaintextCorpusReader(corpus_root, ['1.txt'])
#corpora.fileids()
myfiles = corpora.words('1.txt')
len(set(myfiles))/len(myfiles)
```

# write string into file, p22
```python
# import codecs # need in python2.*
text_file = codecs.open(r"text/2.txt", "w", encoding='utf-8')
test = """Springer Handbook provides a concise compilation of approved key information on methods of research, general principles, and functional relationships in physical and applied sciences.
The world’s leading experts in the fields of physics and engineering will be assigned by one or several renowned editors to write the chapters comprising each volume. The content is selected by these experts from Springer sources (books, journals, online content) and other systematic and approved recent publications of scientific and technical information. This handbook contains 3 volumes.
"""
for w in test:
    text_file.write(w)
text_file.close()
```

# ngrams, p23
```python
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
```

# read excel with xlsxwriter, p25
```python
import xlsxwriter
words = ['automated security monitor', 'chain infection', 'classified data', 'computer vaccine', 'confidentiality', 'cross infection', 'cryptographic facility']
workbook = xlsxwriter.Workbook(r'text/4.xlsx')
sheet = workbook.add_worksheet()
a = 0
b = 0
for w in words:
    sheet.write(a, b, w)
    a = a + 1
workbook.close()
```

# tag, p49
```python
import nltk
from nltk.corpus import brown, PlaintextCorpusReader


corpora = PlaintextCorpusReader(r'C:\Users\\acer\Desktop\corpus _python\\text', ['1.txt'])
text = corpora.raw('1.txt')
tokens = nltk.word_tokenize(text)
brown_tagged_sents = brown.tagged_sents()  
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)  # train
tagged_text = unigram_tagger.tag(tokens)
print(tagged_text)
```

# type, p57
```python
import nltk
from nltk.corpus import PlaintextCorpusReader
corpus_root = r"NlTK\text"
corpora = PlaintextCorpusReader(corpus_root, ['NlTK\text\1.txt'])
corpora.fileids()
myfiles = corpora.words('1.txt')   # myfiles = nltk.Text(corpora.words('1.txt')) in the text
print(len(myfiles), len(set(myfiles)), len(myfiles)/len(set(myfiles)))
```

# wordcloud, p82
```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt  # matplotlib knowledge needed
text = open(r"C:\Users\acer\Desktop\corpus _python\text\\1.txt").read()
wordcloud = WordCloud(background_color='white').generate(text)
plt.imshow(wordcloud.recolor(random_state=2017))
plt.title('Most Frequent Words')
plt.axis('off')
plt.show()
```



