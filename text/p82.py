from wordcloud import WordCloud
import matplotlib.pyplot as plt
text = open(r"C:\Users\acer\Desktop\corpus _python\text\\1.txt").read()
wordcloud = WordCloud(background_color='white').generate(text)
plt.imshow(wordcloud.recolor(random_state=2017))
plt.title('Most Frequent Words')
plt.axis('off')
plt.show()