from nltk.corpus import stopwords, PlaintextCorpusReader
from nltk.probability import FreqDist
from multiprocessing import Process, Queue
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
        # n3 = sorted(list(set(n2)))
        return n2

    @property
    def freq_list(self):
        fdist = FreqDist(self.nor_copora)
        word_list = list(fdist.keys())
        count_list = list(fdist.values())
        pair = zip(word_list, count_list)
        pair_freq = sorted(pair, key=lambda max: -max[1])
        return pair_freq

    def count_words(self, files, coporas, word_to_count):
        count_list = [['filesnames'] + word_to_count]
        for _ in range(len(coporas)):
            fdist = FreqDist(_)
            count = [files(_)]
            for _ in range(len(word_to_count)):
                count += [fdist(word_to_count(_))]
            count_list += [count]
        return count_list
    
    # use muti-processing to increase efficiency
    def count_word(self, file, copora, word_to_count, result_queue):
        count = [file]
        for _ in range(len(word_to_count)):
            count += [fdist(word_to_count(_))]
        return count

    def count_word_processes(self, files, coporas, word_to_count):
        count_list = [['filesnames'] + word_to_count]
        processes = []
        result_queue = Queue()
        for _ in range(len(coporas)):
            p = Process(target=count_word, args=files(_), coporas(_), word_to_count, result_queue)
            processes.append(p)
            p.start()
        for p in processes:
            p.join()
        count_list += result_queue.get()
        return count_list


           
def upload_corpus(root, file):
    copora = nltk.Text(PlaintextCorpusReader(root, file).words())
    return copora


def upload_all(root, '.*'):
    text = []
    f = nltk.Text(PlaintextCorpusReader(root, '.*')
    files = corpora.fileids()
    for file in range(len(files)):
        coporas += f.raw(files(file)).words()
    return files, coporas
        

def output_excel(terms, filepath):
    app = xw.App(visible=False, add_book=False)
    wb = app.books.add()
    sht1 = wb.sheets('sheet1')
    for _ in terms:
        if isinstance(_, list or tuple):
            sht1.range('A1').options(expand='table').value = terms
        else:
            break
    sht1.range('A1').options(transpose=True).value = terms
    wb.save(filepath)
    wb.close()


def main_freq():
    copora = upload_corpus(r'NlTK\text', '1.txt')
    terms = CoporaHandler()
    terms.text = copora
    output_excel(
        list(set(terms.nor_copora)),
        r'C:\Users\acer\Desktop\corpus _python\xlsx_test\excel_output_terms.xlsx'
    )
    

if __name__ == "__main__":
    main()
