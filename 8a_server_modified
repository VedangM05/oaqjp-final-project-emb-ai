"""
Server script for the Emotion Detection application.
Runs a Flask server providing emotion analysis via an API.
"""
from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detect_route():
    """
    Route for emotion detection analysis.
    Accepts textToAnalyze query parameter.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!", 400

    try:
        result = emotion_detector(text_to_analyze)
    except Exception: # pylint: disable=broad-except
        return "Internal Server Error! Please try again later.", 500

    if result is None or result['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    response_str = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return response_str

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
