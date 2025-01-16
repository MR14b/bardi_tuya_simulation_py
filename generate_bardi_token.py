import time
import random
import requests

def generate_door_token():
    return f"door_token_{random.randint(1000, 9999)}"

while True:
    door_token = generate_door_token()
    print(f"Generated door token: {door_token}")
    requests.post("http://localhost:5000/upload_token", json={"door_token": door_token})
    time.sleep(5)  # Simulate trigger every 5 seconds
