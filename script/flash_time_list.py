import requests
import time
url = "http://192.168.10.30:8000/api/tc/"

while True:
    try:
        r = requests.get(url)
    except:
        pass
    finally:
        time.sleep(60)