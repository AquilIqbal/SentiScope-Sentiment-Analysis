from ml.predictor import predict_sentiment as ml_predict_sentiment


def analyze_review(review: str) -> dict:
    """Analyze a customer review using the trained sentiment model."""
    if review is None or not isinstance(review, str) or not review.strip():
        return {
            "success": False,
            "message": "Review cannot be empty."
        }

    return ml_predict_sentiment(review.strip())
