from nltk.corpus import stopwords, PlaintextCorpusReader
import nltk
import xlwings as xw


class CoporaHandler(object):

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, copora):
        if not isinstance(copora, nltk.text.Text):
            raise ValueError('copora must be NLTK text')
        self._text = copora

    @property
    def nor_copora(self):
        stop_words = stopwords.words('english')
        n1 = [word.lower() for word in self._text if word.isalpha()]
        n2 = [word for word in n1 if word not in stop_words]
        n3 = sorted(list(set(n2)))
        return n3


def upload_corpus(root, file):
    copora = nltk.Text(PlaintextCorpusReader(root, file).words())
    return copora


def output_excel(terms, filepath):
    app = xw.App(visible=False, add_book=False)
    wb = app.books.add()
    sht1 = wb.sheets('sheet1')
    sht1.range('A1').options(transpose=True).value = terms
    wb.save(filepath)
    wb.close()


def main():
    copora = upload_corpus(r'NlTK\text', '1.txt')
    terms = CoporaHandler()
    terms.text = copora
    output_excel(
        terms.nor_copora,
        r'C:\Users\acer\Desktop\corpus _python\xlsx_test\excel_output_terms.xlsx'
    )


if __name__ == "__main__":
    main()
