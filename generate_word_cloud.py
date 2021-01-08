from wordcloud import WordCloud
import argparse

uninteresting_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
parser = argparse.ArgumentParser("description='file containing words to create cloud from'")
parser.add_argument('filename')
args = parser.parse_args()
words_file = open(args.filename, "r")

word_array = []
word_count = {}
for sentence in words_file:
    for word in sentence.split():
        word = word.lower()

        if (word.isalpha() )and (word not in uninteresting_words):
            word_array.append(word)
            word_array.sort()
for word in word_array:
    word_count[word] = word_array.count(word)
cloud = WordCloud(width=2560,height=1600,background_color='white').generate_from_frequencies(word_count)
cloud.to_file("wordCloud.jpg")
