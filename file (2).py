import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

# Завантаження ресурсів NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Зчитування тексту з файлу
input_file_path = 'ваш_файл.txt'
with open(input_file_path, 'r', encoding='utf-8') as file:
    original_text = file.read()

# Токенізація по словам
tokens = word_tokenize(original_text)

# Лемматизація
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

# Стеммінг
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in tokens]

# Видалення стоп-слів
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in lemmatized_tokens if token.lower() not in stop_words]

# Видалення пунктуації
filtered_tokens = [token for token in filtered_tokens if token not in string.punctuation]

# Запис обробленого тексту у інший файл
output_file_path = 'оброблений_текст.txt'
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(' '.join(filtered_tokens))
