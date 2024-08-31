import requests

def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }    
    data = { 
        "raw_document": { 
            "text": text_to_analyze 
        } 
    }

    response = requests.post(url,headers=headers,json=data)

    if response.status_code == 200:
        response_json = response.json()
        emotions = response_json.get("emotionPredictions", [])
        if emotions:
            emotion_data = emotions[0]
            emotion = emotion_data.get('emotion',{})
            anger_score = emotion.get('anger',0)
            disgust_score = emotion.get('disgust',0)
            fear_score = emotion.get('fear',0)
            joy_score = emotion.get('joy',0)
            sadness_score = emotion.get('sadness',0)
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            dominant_emotion = max(emotion_scores,key=emotion_scores.get)
            return {'anger': anger_score,
                    'disgust': disgust_score,
                    'fear': fear_score,
                    'joy': joy_score,
                    'sadness': sadness_score,
                    'dominant_emotion': dominant_emotion
                }
    else:
        return f"Error: {response.status_code} - {response.json()}"
