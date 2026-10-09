import json
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

from nlp.textcleaning import clean_text


# Load intents dataset
with open("nlp/intents.json", "r") as file:
    data = json.load(file)


# Store training data
sentences = []
labels = []


# Extract patterns and tags
for intent in data["intents"]:

    tag = intent["tag"]

    for pattern in intent["patterns"]:

        cleaned_pattern = clean_text(pattern)

        sentences.append(cleaned_pattern)

        labels.append(tag)


# Convert text into numerical vectors
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(sentences)


# Train ML model
model = MultinomialNB()

model.fit(X, labels)


# Save model
joblib.dump(model, "nlp/mlmodel.pkl")

# Save vectorizer
joblib.dump(vectorizer, "nlp/vectorizer.pkl")


print("Model trained successfully!")