def classify(score, threshold=0.5):
    """Classify a score into one of two classes."""
    return int(score >= threshold)
