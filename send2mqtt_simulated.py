import time

while True:
    door_token = "sample_door_token"
    datetime_now = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Success: Sent {door_token} and {datetime_now} to MQTT broker")
    time.sleep(5)  # Simulate every 5 seconds
