from nltk.book import *

# search text
text1.concordance('Monstrous')  # text1 is an instance of 'nltk.text.Text'
text1.similar('Monstrous')  # other words appear in the similar range of contest
text1.common_contexts(['monstrous', 'very']) # examine just the contexts that are shared by two or more words

text4.dispersion_plot(
    ['citizens', 'democracy', 'freedom', 'duties', 'America'])
