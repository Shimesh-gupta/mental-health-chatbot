def sentiment_analysis(message):
    """Basic sentiment analysis stub."""
    if "sad" in message or "depressed" in message:
        return "negative"
    elif "happy" in message or "good" in message:
        return "positive"
    return "neutral"