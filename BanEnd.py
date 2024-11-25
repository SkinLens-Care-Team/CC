from flask import Flask, request, jsonify
import requests  

app = Flask(__name__)

MODEL_API_URL = "http://[YOUR_COMPUTE_ENGINE_IP]:8080/predict"

@app.route('/get-prediction', methods=['POST'])
def get_prediction():
    image = request.files['image']
    
    response = requests.post(MODEL_API_URL, files={'image': image})
    
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
