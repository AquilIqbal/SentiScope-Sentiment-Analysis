"""
SentiScope Sentiment Predictor

Loads the trained model and TF-IDF vectorizer
and predicts the sentiment of a review.
"""

from pathlib import Path

import joblib

from ml.preprocessing.text_preprocessor import clean_text


# ----------------------------------------------------------
# Model Paths
# ----------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "sentiment_model.pkl"
VECTORIZER_PATH = BASE_DIR / "models" / "tfidf_vectorizer.pkl"


# ----------------------------------------------------------
# Load Model Once
# ----------------------------------------------------------

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


# ----------------------------------------------------------
# Prediction Function
# ----------------------------------------------------------

def predict_sentiment(review: str) -> dict:
    """
    Predict sentiment for a customer review.

    Parameters
    ----------
    review : str

    Returns
    -------
    dict
    """

    if not review.strip():
        return {
            "success": False,
            "message": "Review cannot be empty."
        }

    # Clean review
    cleaned = clean_text(review)

    # Convert to TF-IDF
    vector = vectorizer.transform([cleaned])

    # # Predict
    # prediction = model.predict(vector)[0]

    # # Confidence
    # probability = model.predict_proba(vector)[0]

    # confidence = float(max(probability) * 100)

    # return {
    #     "success": True,
    #     "review": review,
    #     "cleaned_review": cleaned,
    #     "sentiment": prediction.capitalize(),
    #     "confidence": round(confidence, 2)
    # }
    
    # Predict probabilities
    probability = model.predict_proba(vector)[0]

    negative_prob = float(probability[0])
    positive_prob = float(probability[1])

    confidence = max(negative_prob, positive_prob) * 100

    # Confidence-based sentiment
    if confidence < 65:
        sentiment = "Neutral"
    elif positive_prob > negative_prob:
        sentiment = "Positive"
    else:
        sentiment = "Negative"

    return {
        "success": True,
        "review": review,
        "cleaned_review": cleaned,
        "sentiment": sentiment,
        "confidence": round(confidence, 2)
    }
    
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

print(model.classes_)