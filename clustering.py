def cluster(values, threshold=5):
    """Group numbers by a threshold."""
    return [int(value >= threshold) for value in values]
