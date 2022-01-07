import time
import requests


while 1:
    resp = requests.get("http://api:8080")
    print(resp.text)
    time.sleep(5)