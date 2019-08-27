from nltk.corpus import stopwords, PlaintextCorpusReader
from nltk.probability import FreqDist
from multiprocessing import Process, Queue
import nltk
import xlwings as xw
'''
以Excel文件格式输出表格
chapter7.2 on P132
试图使用多线程提高运行效率
'''


class CoporaHandler(object):
    def __init__(self, filenames, raw_corpora, word_to_count):
        self.raw_corpora = raw_corpora
        self.filenames = filenames
        self.word_to_count = word_to_count

    @property
    def corpora(self):
        n2 = []
        for _ in self.raw_corpora:
            n1 = [word.lower() for word in _ if word.isalpha()]
            n2 += [n1]
        return n2

    def count_word(self, filename, corpora, word_to_count, result_queue):
        count = [filename]
        fdist = FreqDist(corpora)
        for _ in word_to_count:
            count += [fdist[_]]
        result_queue.put(count)

    def combine(self, result_queue):
        while True:
            
""" 
    def count_word_processes(self):
        count_list = [['filesnames'] + self.word_to_count]
        result_queue = Queue()
        processes = []
        for _ in range(len(self.corpora)):
            p = Process(
                target=self.count_word,
                args=(self.filenames[_], self.corpora[_], self.word_to_count, result_queue))
            processes.append(p)
            p.start()
        for p in processes:
            p.join()
        count_list += result_queue.get()
        return count_list

 """
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
    word_to_count = [
        'can', 'could', 'may', 'might', 'must', 'will', 'shall', 'should'
    ]
    terms = CoporaHandler(filenames, corpora, word_to_count)
    output_excel(
        terms.count_word_processes(),
        r'C:\Users\acer\Desktop\corpus _python\xlsx_test\excel_output_spreadsheet.xlsx'
    )


if __name__ == "__main__":
    main()
