import requests
import json
import time
import RPi.GPIO as GPIO
server = "http://192.168.10.11:8000/"

port = [1]
state = 0
typed = 0
change = 1
#gpio = [11, 12, 13, 15, 16, 18, 22, 7, 29, 31, 33, 35, 37, 32, 36, 38, 40]


def stat():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    if typed:
        GPIO.setup(11, GPIO.IN)
    else:
        GPIO.setup(11, GPIO.OUT)

def get_data(port):
    global state,typed,change
    url = server + 'api/id/%s' % port
    r = requests.get(url)
    data = json.loads(r.text)
    state = data['state']
    typed = data['type']
    change = data['change']

    
def apply():
    global state,typed,change
    mid = -1
    if not typed:
        GPIO.output(11, state)
        print(11, state)
    if typed:
        while True:
            state = GPIO.input(11)
            time.sleep(1)
            if not state == mid:
                r = requests.get(server + 'api/cn/1/'+ str(state))
                mid = state
                print(11,state,r.status_code)
            


get_data(1)
stat()
apply()
while True:
    get_data(1)
    if change:
        apply()
    time.sleep(1)
    
