import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# Завантаження тексту з Project Gutenberg
nltk.download('gutenberg')
file_id = 'austen-sense.txt'
text = gutenberg.raw(file_id)

# Токенізація тексту на слова
words = nltk.word_tokenize(text)

# Визначення кількості слів у тексті
num_words = len(words)
print(f"Кількість слів у тексті: {num_words}")

# Визначення 10 найбільш вживаних слів у тексті
fdist = FreqDist(words)
top_words = fdist.most_common(10)
print("10 найбільш вживаних слів:")
for word, frequency in top_words:
    print(f"{word}: {frequency}")

# Побудова стовпчастої діаграми для найбільш вживаних слів
plt.bar(range(10), [freq for word, freq in top_words], tick_label=[word for word, freq in top_words])
plt.title('Найбільш вживані слова у тексті')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.show()
