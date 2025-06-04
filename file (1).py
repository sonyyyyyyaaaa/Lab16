import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import matplotlib.pyplot as plt

# Завантаження тексту з Project Gutenberg
nltk.download('gutenberg')
nltk.download('stopwords')
file_id = 'austen-sense.txt'
text = gutenberg.raw(file_id)

# Токенізація тексту на слова
words = word_tokenize(text)

# Видалення стоп-слів та пунктуації
stop_words = set(stopwords.words('english'))
filtered_words = [word.lower() for word in words if (word.isalpha() and word.lower() not in stop_words)]

# Визначення 10 найбільш вживаних слів у відфільтрованому тексті
fdist_filtered = FreqDist(filtered_words)
top_filtered_words = fdist_filtered.most_common(10)
print("10 найбільш вживаних слів після видалення стоп-слів та пунктуації:")
for word, frequency in top_filtered_words:
    print(f"{word}: {frequency}")

# Побудова стовпчастої діаграми для найбільш вживаних слів у відфільтрованому тексті
plt.bar(range(10), [freq for word, freq in top_filtered_words], tick_label=[word for word, freq in top_filtered_words])
plt.title('Найбільш вживані слова після видалення стоп-слів та пунктуації')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.show()
