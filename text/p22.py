import codecs
text_file = codecs.open(r"text/2.txt", "w", encoding='utf-8')
test = """Springer Handbook provides a concise compilation of approved key information on methods of research, general principles, and functional relationships in physical and applied sciences.
The world’s leading experts in the fields of physics and engineering will be assigned by one or several renowned editors to write the chapters comprising each volume. The content is selected by these experts from Springer sources (books, journals, online content) and other systematic and approved recent publications of scientific and technical information. This handbook contains 3 volumes.
"""
for w in test:
    text_file.write(w)
text_file.close()