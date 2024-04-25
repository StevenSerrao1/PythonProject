import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text)
    
    # Extract emotion predictions
    emotion_predictions = formatted_response.get('emotionPredictions', [])
    if emotion_predictions:
        # Extract emotions and their scores from the first prediction
        emotion_prediction = emotion_predictions[0].get('emotion', {})
        if emotion_prediction:
            emotions_dict = {
                'anger': emotion_prediction.get('anger', 0),
                'disgust': emotion_prediction.get('disgust', 0),
                'fear': emotion_prediction.get('fear', 0),
                'joy': emotion_prediction.get('joy', 0),
                'sadness': emotion_prediction.get('sadness', 0),
            }
            # Find the dominant emotion
            dominant_emotion = max(emotions_dict, key=emotions_dict.get)
            
            return {
                'emotions': emotions_dict,
                'dominant_emotion': dominant_emotion,
            }
    
    return {'error': 'No emotion predictions found in the response.'}

# Example usage:
# result = emotion_detector('I love this new technology.')
# print(result)
