import re

regex = re.compile(r"(.*?)([\.](\r\n)+)")

test_str = "The American Copyright Act\r\n\r\nChapter 1 Subject Matter and Scope of Copyright\r\n$ 101 Definitions.\r\n\r\nExcept as otherwise provided in this'\r\n title, as used in this.\r\n title, the following terms and thier variant forms mean the folowing:\r\n"

matches = re.findall(regex, test_str)

regex2 = re.sub(r'[.]?(\r\n)+', '.', test_str)
print(regex2)

regex3 = re.sub(r'((\.(\r\n)+)|([:\'\"]?(\r\n)+))', '.', test_str)
print(regex3)
