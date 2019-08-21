from urllib import request
from nltk.corpus import stopwords
import nltk
import xlwings as xw


def corpus_sourcing(url):
    response = request.urlopen(url)
    raw = response.read().decode('utf-8')
    tokens = nltk.word_tokenize(raw)

    def normalization(text):
        stop_words = stopwords.words('english')
        n1 = [word.lower() for word in text if word.isalpha()]
        n2 = [word for ]



def main(terms, file):
    wb = xw.Book(file)
    sht = wb.sheets['sheet1']




    