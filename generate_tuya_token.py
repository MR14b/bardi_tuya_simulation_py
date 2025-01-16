from flask import Flask, request, jsonify
import threading
import time
import random

app = Flask(__name__)
tuya_token = None

def generate_tuya_token():
    global tuya_token
    while True:
        tuya_token = f"tuya_token_{random.randint(1000, 9999)}"
        print(f"Generated tuya token: {tuya_token}")
        time.sleep(10)  # Simulate every 10 seconds

@app.route('/upload_token', methods=['POST'])
def upload_token():
    data = request.json
    print(f"Received door token: {data['door_token']}")
    return jsonify(success=True)

if __name__ == "__main__":
    threading.Thread(target=generate_tuya_token).start()
    app.run(port=5000)
