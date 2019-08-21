dict = {'Name': 'Runoob', 'Age': 7}
freq = dict.items()
list1 = []
list2 = []
for i in range(len(freq)):
    list1 += [freq[i][0]]
    list2 += [freq[i][0]]
print(list1, list2)
