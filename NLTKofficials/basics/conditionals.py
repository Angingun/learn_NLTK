# Conditionals

sent7 = [
    'Pierre', 'Vinken', ',', '61', 'years', 'old', ',', 'will', 'join', 'the',
    'board', 'as', 'a', 'nonexecutive', 'director', 'Nov.', '29', '.'
]
[w for w in sent7
       if len(w) < 4]  # [',', '61', 'old', ',', 'the', 'as', 'a', '29', '.']


# Some Word Comparison Operators

s.startswith(t)  # test if s starts with t
s.endswith(t)  # test if s ends with t
t in s  # test if t is a substring of s
s.islower()  # test if s contains cased characters and all are lowercase
s.isupper()  # test if s contains cased characters and all are uppercase
s.isalpha()  # test if s is non-empty and all characters in s are alphabetic
s.isalnum()  # test if s is non-empty and all characters in s are alphanumeric
s.isdigit()  # test if s is non-empty and all characters in s are digits
s.istitle(
)  # test if s contains cased characters and is titlecased (i.e. all words in s have initial capitals)
