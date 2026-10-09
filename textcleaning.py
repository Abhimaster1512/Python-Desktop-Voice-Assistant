import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Download resources only first time
nltk.download("stopwords")
nltk.download("wordnet")


lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words("english"))


def clean_text(text):

    # Convert lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Split words
    words = text.split()

    # Remove stop words and lemmatize
    cleaned_words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(cleaned_words)
