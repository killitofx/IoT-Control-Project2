import requests
import json
import RPi.GPIO as GPIO
server = "http://192.168.10.11:8000/"

port = [1]
gpio = [11, 12, 13, 15, 16, 18, 22, 7, 29, 31, 33, 35, 37, 32, 36, 38, 40]
state = []
typed = []



def get_data(port):
    url = server + 'api/id/%s' % port
    r = requests.get(url)
    data = json.loads(r.text)
    state.append(data['state'])
    type.append(data['type'])


def stat():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    for i in range (0,len(typed)):
        if typed[i]:
            GPIO.setup(gpio[i], GPIO.IN)
        else:
            GPIO.setup(gpio[i], GPIO.OUT)

def apply():
    for i in range(0, len(state)):
        if not typed[i]:
            GPIO.output(gpio[i], state[i])
        if typed[i]:
            state = GPIO.input(gpio[i])
            r = requests.get(server + '/api/cn/' + port[i] + state)
            print(r.status_code)
