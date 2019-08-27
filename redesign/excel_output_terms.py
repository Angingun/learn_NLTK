from nltk.corpus import stopwords, PlaintextCorpusReader
import nltk
import xlwings as xw
'''
以Excel文件格式输入术语（类符）
chapter7.1.1 on P125
'''


class CorporaHandler(object):
    def __init__(self, text):
        self.text = text

    def nor_corpora(self):
        stop_words = stopwords.words('english')
        n1 = [word.lower() for word in self.text if word.isalpha()]
        n2 = [word for word in n1 if word not in stop_words]
        n3 = sorted(list(set(n2)))
        return n3


def upload_corpus(root, file):
    corpora = PlaintextCorpusReader(root, file).words()
    return corpora


def output_excel(terms, filepath):
    app = xw.App(visible=False, add_book=False)
    wb = app.books.add()
    sht1 = wb.sheets('sheet1')
    sht1.range('A1').options(transpose=True).value = terms
    wb.save(filepath)
    wb.close()


def main():
    corpora = upload_corpus(r'NlTK\text', '1.txt')
    terms = CorporaHandler(corpora)
    output_excel(
        terms.nor_corpora(),
        r'C:\Users\acer\Desktop\corpus _python\xlsx_test\excel_output_terms.xlsx'
    )


if __name__ == "__main__":
    main()
