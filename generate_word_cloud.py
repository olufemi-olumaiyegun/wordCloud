from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
words_file = open("words.txt", "r")
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
print(word_count)
cloud = WordCloud().generate_from_frequencies(word_count)
plt.figure(figsize=(10,10),facecolor=None)
plt.imshow(cloud)
plt.axis("off")
plt.show()
