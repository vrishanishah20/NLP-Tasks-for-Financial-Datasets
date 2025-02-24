import nltk
from nltk import word_tokenize, sent_tokenize

# nltk.download()

# nltk.download('punkt', download_dir = '/Users/vrishfish/Intro to NLP/nltk_data', force=True)
print(nltk.data.path)
print(nltk.data.find('tokenizers/punkt'))

text = "This is my introduction to NLP tasks."
print(word_tokenize(text))  # ✅ Should work now
