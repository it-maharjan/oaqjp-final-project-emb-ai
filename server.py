from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the emotion detection API with the /emotionDetector endpoint
@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    text = request.args.get('textToAnalyze', '') 
    result = emotion_detector(text)
    if result['dominant_emotion']:
        return jsonify(result)   
    else:
        return '<b>Invalid text! Please try again!</b>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
