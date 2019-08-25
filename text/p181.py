with open(r'NlTK\text\sl.txt', 'r', encoding='utf-8') as fe:
    fe_lines = fe.readlines()

with open(r'NlTK\text\tl.txt', 'r', encoding='utf-8') as fc:
    fc_lines = fc.readlines()

l1 = list(zip(fe_lines, fc_lines))

with open(r'NlTK\text\sltl.txt', 'a', encoding='utf-8') as fec:
    for _ in l1:
        fec.write(''.join(_))
