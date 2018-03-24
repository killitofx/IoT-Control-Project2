from urllib import urequest
from machine import Pin
import json
import time



device_id_1 = 1
device_id_2 = 2
device_id_3 = 3
device_id_4 = 4
url = "http://192.168.10.30:8000/api/"


a = 0
b = 0
c = 0
d = 0
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
    try:
        f = urequest.urlopen(url + 'id/' + str(device_id_1))
        #print ("http get")
        data = f.read()
        data = json.loads(data)
        # port_id_1 = data['id']
        is_change_1 = data['change']
        port_state_1 = data["state"]
        port_type_1 = data['type']

        if device_id_2:
            g = urequest.urlopen(url + 'id/' + str(device_id_2))
            data_2 = g.read()
            data_2 = json.loads(data_2)
            is_change_2 = data_2['change']
            port_state_2 = data_2["state"]
            port_type_2 = data_2['type']

        if device_id_3:
            h = urequest.urlopen(url + 'id/' + str(device_id_3))
            data_3 = h.read()
            data_3 = json.loads(data_3)
            is_change_3 = data_3['change']
            port_state_3 = data_3["state"]
            port_type_3 = data_3['type']

        if device_id_4:
            h = urequest.urlopen(url + 'id/' + str(device_id_4))
            data_4 = h.read()
            data_4 = json.loads(data_4)
            is_change_4 = data_4['change']
            port_state_4 = data_4["state"]
            port_type_4 = data_4['type']

        if port_type_1 == 0:
            if a == 0:
                print ("init1 out")
                p1 = Pin(5, Pin.OUT)
                p1(port_state_1)
                a = 1
            else:
                if is_change_1 == 1:
                    print ("apply data 1:%d" % port_state_1)
                    p1(port_state_1)
                    urequest.urlopen(url + 'cgc/' + str(device_id_1))

        if port_type_1 == 1:
            print ("init1 in")
            p1 = Pin(5, Pin.IN)
            state_1 = p1()
            # print ("state:%s" % state_1)
            x = urequest.urlopen(url + "cn/" + str(device_id_1) + '/' + str(state_1))
            # i = 1
            # p2.irq(trigger=Pin.IN, handler=call_back_1)

        if device_id_2:
            if port_type_2 == 0:
                if b == 0:
                    print ("init2 out")
                    p2 = Pin(4, Pin.OUT)
                    p2(port_state_2)
                    b = 1
                else:
                    if is_change_2 == 1:
                        print ("apply data 2:%d" % port_state_2)
                        p2(port_state_2)
                        urequest.urlopen(url + 'cgc/' + str(device_id_2))

            if port_type_2 == 1:
                print ("init2 in")
                p2 = Pin(4, Pin.IN)
                state_2 = p2()
                x = urequest.urlopen(url + "cn/" + str(device_id_2) + '/' + str(state_2))


        if device_id_3:
            if port_type_3 == 0:
                if c == 0:
                    print ("init3 out")
                    p3 = Pin(0, Pin.OUT)
                    p3(port_state_3)
                    c = 1
                else:
                    if is_change_3 == 1:
                        print ("apply data 3:%d" % port_state_3)
                        p3(port_state_3)
                        urequest.urlopen(url + 'cgc/' + str(device_id_3))

            if port_type_3 == 1:
                print ("init3 in")
                p3 = Pin(0, Pin.IN)
                state_3 = p3()
                x = urequest.urlopen(url + "cn/" + str(device_id_3) + '/' + str(state_3))

        if device_id_4:
            if port_type_4 == 0:
                if d == 0:
                    print ("init4 out")
                    p4 = Pin(2, Pin.OUT)
                    p4(port_state_4)
                    d = 1
                else:
                    if is_change_4 == 1:
                        print ("apply data 4:%d" % port_state_4)
                        p4(port_state_4)
                        urequest.urlopen(url + 'cgc/' + str(device_id_4))

            if port_type_4 == 1:
                print ("init4 in")
                p4 = Pin(2, Pin.IN)
                state_4 = p4()
                x = urequest.urlopen(url + "cn/" + str(device_id_3) + '/' + str(state_4))

        time.sleep(1)
    except:
        time.sleep(1)




