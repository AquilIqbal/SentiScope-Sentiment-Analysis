"""
Text Preprocessor for SentiScope

This module contains reusable text preprocessing functions used during
both model training and inference.
"""

import re
import string

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Initialize NLP Resources
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def clean_text(text: str) -> str:
    """
    Clean and preprocess review text.

    Steps:
    - Remove HTML tags
    - Convert to lowercase
    - Remove punctuation
    - Remove numbers
    - Remove extra spaces
    - Remove stopwords
    - Lemmatize words

    Parameters
    ----------
    text : str
        Raw review text.

    Returns
    -------
    str
        Cleaned review text.
    """

    if not isinstance(text, str):
        return ""

    # Remove HTML tags
    text = re.sub(r"<.*?>", " ", text)

    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    # Remove numbers
    text = re.sub(r"\d+", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    words = text.split()

    cleaned_words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(cleaned_words)