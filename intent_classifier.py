import joblib
from nlp.textcleaning import clean_text


# Load trained ML model
model = joblib.load("nlp/mlmodel.pkl")

# Load TF-IDF vectorizer
vectorizer = joblib.load("nlp/vectorizer.pkl")


def predict_intent(command):

    # Clean user command
    cleaned_text = clean_text(command)

    # Convert text into vector
    vector = vectorizer.transform([cleaned_text])

    # Get confidence scores
    probabilities = model.predict_proba(vector)

    confidence = probabilities.max()

    # Predict intent
    intent = model.predict(vector)[0]

    return intent, confidence