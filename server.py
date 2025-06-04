''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Error: No 'textToAnalyze' parameter provided.", 400  # HTTP 400 Bad Request

    try:
        response = sentiment_analyzer(text_to_analyze)
    except Exception as e:
        return f"Error processing sentiment: {str(e)}", 500

    label = response.get('label')
    score = response.get('score')
    if label is None:
        return "Invalid input! Try again.", 400

    return f"The given text has been identified as {label} with a score of {score}."

@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
