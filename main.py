import re
import nltk
nltk.download('vader_lexicon')
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

with open("miracle_in_the_andes.txt", "r") as file:
    book = file.read()


pattern = re.compile("[a-z]+")
findings = re.findall(pattern, book.lower())

d = {}
for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

d_list = [(value, key) for (key, value) in d.items()]
d_list = sorted(d_list, reverse=True)
print(d_list[:5])

english_stopwords = stopwords.words("english")

filteres_words = []
for count, word in d_list:
    if word not in english_stopwords:
        filteres_words.append((count, word))

print(filteres_words[:10])

analyzer = SentimentIntensityAnalyzer()
result = analyzer.polarity_scores("Hey, look how bad the trees are.")
print(result)

pattern = re.compile("Chapter [0-9]+")
chapters = re.split(pattern, book)
chapters = chapters[1:]
print(chapters)

for index, chapter in enumerate(chapters):
    score = analyzer.polarity_scores(chapter)
    print(index + 1, score)