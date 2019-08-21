from nltk.corpus import PlaintextCorpusReader, stopwords
# from nltk.stem import WordNetLemmatizer
import nltk
import xlsxwriter


def upload_corpus(root, name):
    corpora = PlaintextCorpusReader(root, [name])
    MyFiles = corpora.words(corpora.fileids())
    return MyFiles


def normalization(text):
    StopWords = set(stopwords.words('english'))
    StopWords.update(['therefo', 'one', 'two'])
    normal1 = [word.lower() for word in text if word.isalpha()]
    normal2 = [word for word in normal1 if word not in StopWords]
    # for i in nltk.pos_tag(normal2):
    #     wnl = WordNetLemmatizer()
    #     normal3 = [wnl.lemmatize(i)]
    return normal2


def get_terms(text):
    terms = sorted(set(text))
    return terms


def term_output(name, data):
    workbook = xlsxwriter.Workbook(name)
    sheet = workbook.add_worksheet()
    a = 0
    b = 0
    for w in data:
        sheet.write(a, b, w)
        a += 1
    workbook.close()


if __name__ == "__main__":
    corpora = r'C:\\Users\\acer\Desktop\corpus _python\text'
    MyFiles = '1.txt'
    output = r'C:\Users\acer\Desktop\corpus _python\text\p127.xlsx'
    step1 = upload_corpus(corpora, MyFiles)
    step2 = normalization(step1)
    step3 = get_terms(step2)
    step4 = term_output(output, step3)