words = ['automated security monitor', 'chain infection', 'classified data', 'computer vaccine', 'confidentiality', 'cross infection', 'cryptographic facility']
import xlsxwriter
workbook = xlsxwriter.Workbook(r'text/4.xlsx')
sheet = workbook.add_worksheet()
a = 0
b = 0
for w in words:
    sheet.write(a, b, w)
    a = a + 1
workbook.close()