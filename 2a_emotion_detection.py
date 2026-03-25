"""
This module provides emotion detection functionality.
It interacts with the IBM Watson NLP EmotionPredict API.
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion of a given text using IBM Watson NLP.
    Returns a dictionary of emotion scores and the dominant emotion.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=input_json, headers=headers, timeout=10)

    if response.status_code == 400:
        return None

    formatted_response = json.loads(response.text)
    # Extract emotions from JSON structure
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Find dominant emotion
    emotion_list = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_list, key=emotion_list.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
