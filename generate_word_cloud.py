from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser("description='file containing words to create cloud from'")
parser.add_argument('filename')
args = parser.parse_args()
words_file = open(args.filename, "r")
stopwords = set(STOPWORDS)
word_array = []
word_count = {}
for sentence in words_file:
    for word in sentence.split():
        if word.isalpha():
            word_array.append(word)
            word_array.sort()
for word in word_array:
    word_count[word] = word_array.count(word)
cloud = WordCloud(width=1000,height=1000,background_color='white').generate_from_frequencies(word_count)
plt.figure(figsize=(10,10),facecolor=None)
plt.imshow(cloud)
plt.axis("off")
plt.show()
