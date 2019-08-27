from nltk.corpus import stopwords, PlaintextCorpusReader
from nltk.probability import FreqDist
from multiprocessing import Process, Queue
import nltk
import xlwings as xw
'''
以Excel文件格式输出表格
chapter7.2 on P132
'''


class CoporaHandler(object):
    def __init__(self, filenames, raw_corpora):
        self.filenames = filenames
        self.raw_corpora = raw_corpora
        
    @property
    def corpora(self):
        n2 = []
        for _ in self.raw_corpora:
            n1 = [word.lower() for word in _ if word.isalpha()]
            n2 += [n1]
        return n2

    def count_words(self, word_to_count):
        count_list = [['filesnames'] + word_to_count]
        for i in range(len(self.corpora)):
            fdist = FreqDist(self.corpora[i])
            count = [self.filenames[i]]
            for j in word_to_count:
                count += [fdist[j]]
            count_list += [count]
        return count_list

    """ # use muti-processing to increase efficiency
    def count_word(self, file, corpora, word_to_count, result_queue):
        count = [file]
        fdist = FreqDist(corpora)
        for _ in word_to_count:
            count += [fdist(_)]
        return count

    def count_word_processes(self, files, corpora, word_to_count):
        count_list = [['filesnames'] + word_to_count]
        processes = []
        result_queue = Queue()
        for _ in range(len(corpora)):
            p = Process(target=count_word, args=files(_), corpora(_), word_to_count, result_queue)
            processes.append(p)
            p.start()
        for p in processes:
            p.join()
        count_list += result_queue.get()
        return count_list """


def upload_all(root):
    f = PlaintextCorpusReader(root, '.*\.txt')
    filenames = f.fileids()
    corpora = list(map(f.words, filenames))
    return filenames, corpora


def output_excel(terms, filepath):
    app = xw.App(visible=False, add_book=False)
    wb = app.books.add()
    sht1 = wb.sheets('sheet1')
    sht1.range('A1').options(expand='table').value = terms
    wb.save(filepath)
    wb.close()


def main():
    filenames, corpora = upload_all(
        r'C:\Users\acer\Desktop\corpus _python\test')
    terms = CoporaHandler(filenames, corpora)
    word_to_count = [
        'can', 'could', 'may', 'might', 'must', 'will', 'shall', 'should'
    ]
    output_excel(
        terms.count_words(word_to_count),
        r'C:\Users\acer\Desktop\corpus _python\xlsx_test\excel_output_spreadsheet.xlsx'
    )


if __name__ == "__main__":
    main()
