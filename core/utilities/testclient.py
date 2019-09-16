import time

from core.utilities.tcp.json.json_client import JsonClient

client = JsonClient().get_instance()
client.connect('127.0.0.1', 5000)

while True:
    client.send_obj({"message": "new connection"})
    print('message')
    time.sleep(2)
