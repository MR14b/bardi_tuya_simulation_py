import time
import requests

while True:
    response = requests.get("http://localhost:5000/latest_door_token")
    if response.status_code == 200:
        door_token = response.json()['door_token']
        print(f"Pulled door token: {door_token}")
    time.sleep(5)  # Pull every 5 seconds
