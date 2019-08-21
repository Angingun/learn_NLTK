from nltk.corpus import PlaintextCorpusReader, stopwords
from nltk import FreqDist
import xlsxwriter


def up_load(root, name):
    corpora = PlaintextCorpusReader(root, [name])
    MyFiles = corpora.words(corpora.fileids())
    return MyFiles


def normalization(text):
    Stopwords = set(stopwords.words('english'))
    normal1 = [word.lower() for word in text if word.isalpha()]
    normal2 = [word for word in normal1 if word not in Stopwords]
    return normal2


def count_word(text):
    freq = FreqDist(text).items()
    word_list = []
    count_list = []
    for key, value in freq:
        word_list.append(key)
        count_list.append(value)
    return word_list, count_list
    # print(word_list, count_list)


def word_freq_pair(word, freq):
    PairList = []
    for i in range(len(word)):
        pair = []
        pair += [word[i], freq[i]]
        PairList += [pair]
    return PairList


def sort_data(word, freq):
    Wordfreqlist = word_freq_pair(word, freq)
    SortedData = sorted(
        Wordfreqlist, key=lambda result: result[1], reverse=True)
    return SortedData


def data_output(name, data):
    Workbook = xlsxwriter.Workbook(name)
    sheet = Workbook.add_worksheet()
    sheet.set_column('A: A', 20)
    a = 0
    b = 0
    for i in range(len(data)):
        sheet.write(a, b, data[i][0])
        sheet.write(a, b + 1, data[i][1])
        a += 0
    Workbook.close()


if __name__ == "__main__":
    corpora = r'C:\Users\acer\Desktop\corpus _python\text'
    name = '1.txt'
    output = r'C:\Users\acer\Desktop\corpus _python\text\p129.xlsx'
    step1 = up_load(corpora, name)
    step2 = normalization(step1)
    step3, step4 = count_word(step2)
    step5 = sort_data(step3, step4)
    step6 = data_output(output, step5)
