from urllib import urequest
from machine import Pin
import json
import time



device_id = 1
url = "http://192.168.10.30:8000/api/"
i = 0
a = -1
p0 = Pin(16, Pin.OUT)
p0(1)
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('TP-LINK_445B', 'jungle00')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    p0(0)

do_connect()

while True:
    f = urequest.urlopen('http://192.168.10.30:8000/api/id/1')
    print ("http get")
    data = f.read()
    data = json.loads(data)
    port_id = data['id']
    is_change = data['change']
    port_state = data["state"]
    port_type = data['type']
    print (port_state)
    if i == 0:
        if port_type == 0:
            print ("init out")
            p2 = Pin(2, Pin.OUT)
            p2(port_state)
            i = 1
        else:
            print ("init in")
            p2 = Pin(2, Pin.IN)
            while True:
                state = p2()
                if a == -1:
                    print ("state:%s" % state)
                    x = urequest.urlopen(url + "cn/" + str(device_id) + '/' + str(state))
                    a = state
                if not a == state:
                    print ("state:%s" % state)
                    x = urequest.urlopen(url + "cn/" + str(device_id) + '/' + str(state))
                    a = state
                time.sleep(1)
    else:
        if is_change == 1:
            print ("apply data")
            p2(port_state)
            urequest.urlopen(url + 'cgc/' + str(device_id))
    time.sleep(1)
    #print ("finish")
