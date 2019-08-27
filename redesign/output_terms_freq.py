from nltk.corpus import stopwords, PlaintextCorpusReader
from nltk.probability import FreqDist

import nltk
import xlwings as xw
'''
按词频输出术语
chapter7.1.2 on P128
'''


class CorporaHandler(object):
    def __init__(self, text):
        self.text = text

    @property
    def nor_corpora(self):
        stop_words = stopwords.words('english')
        n1 = [word.lower() for word in self.text if word.isalpha()]
        n2 = [word for word in n1 if word not in stop_words]
        return n2

    def freq_list(self):
        fdist = FreqDist(self.nor_corpora)
        word_list = list(fdist.keys())
        count_list = list(fdist.values())
        pair = zip(word_list, count_list)
        pair_freq = sorted(pair, key=lambda max: -max[1])
        return pair_freq


def upload_corpus(root, file):
    corpora = PlaintextCorpusReader(root, file).words()
    return corpora


def output_excel(terms, filepath):
    app = xw.App(visible=False, add_book=False)
    wb = app.books.add()
    sht1 = wb.sheets('sheet1')
    sht1.range('A1').options(expand='table').value = terms
    wb.save(filepath)
    wb.close()


def main():
    corpora = upload_corpus(r'NlTK\text', '1.txt')
    terms = CorporaHandler(corpora)
    output_excel(
        terms.freq_list(),
        r'C:\Users\acer\Desktop\corpus _python\xlsx_test\excel_output_freq.xlsx'
    )

if __name__ == "__main__":
    main()