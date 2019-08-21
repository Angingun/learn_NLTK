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