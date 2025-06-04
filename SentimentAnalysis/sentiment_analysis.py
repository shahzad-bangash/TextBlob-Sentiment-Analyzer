from textblob import TextBlob

def sentiment_analyzer(text_to_analyse):
    """
    Analyzes the sentiment of the provided text using TextBlob.

    Args:
        text_to_analyse (str): The text to analyze.

    Returns:
        dict: A dictionary with 'label' and 'score' keys.
    """
    blob = TextBlob(text_to_analyse)
    polarity = blob.sentiment.polarity

    # Assign label based on polarity value
    if polarity > 0:
        label = "POSITIVE"
    elif polarity < 0:
        label = "NEGATIVE"
    else:
        label = "NEUTRAL"

    return {'label': label, 'score':  round(abs(polarity), 4)}

