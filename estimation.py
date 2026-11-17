def mean_absolute_error(actual, predicted):
    """Calculate mean absolute error."""
    if len(actual) != len(predicted) or not actual:
        raise ValueError("Input lists must have equal nonzero lengths")
    return sum(abs(a - p) for a, p in zip(actual, predicted)) / len(actual)
