import time
import requests

while True:
    response = requests.get("http://localhost:5000/tuya_token")
    if response.status_code == 200:
        print(f"Keep-alive check successful: {response.json()['tuya_token']}")
    time.sleep(5)  # Check every 5 seconds
