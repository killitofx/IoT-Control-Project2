import socket
import json

device_id = 1
active_data = {"id": device_id, "method": "alive"}
apply_data = {"id": device_id, "method": "apply"}

#
# ##########micropython专用函数##########
# # 连接网络
# from machine import Pin
# p0 = Pin(16, Pin.OUT)
# p0(1)
# def do_connect():
#     import network
#     sta_if = network.WLAN(network.STA_IF)
#     if not sta_if.isconnected():
#         print('connecting to network...')
#         sta_if.active(True)
#         sta_if.connect('TP-LINK_445B', 'jungle00')
#         while not sta_if.isconnected():
#             pass
#     print('network config:', sta_if.ifconfig())
#     p0(0)
#
# do_connect()
#
#
# #应用状态
#
# def apply_state(port_type ,state=0):
#     p1 = Pin(5, Pin.OUT)
#     p1(state)
#

##########通用函数##########
def enc(data):
    data = json.dumps(data)
    data = data.encode()
    return data



def main():
    data = enc(active_data)
    s.sendto(data, ('127.0.0.1', 9999))
    while True:
        rec_data = s.recv(1024).decode('utf-8')
        rec_data = json.loads(rec_data)
        if rec_data['id'] == device_id:
            port_type = rec_data['type']
            port_state = rec_data['state']
            ##########
            # apply_state(port_state)
            print(rec_data)
            ##########
            data = enc(apply_data)
            s.sendto(data, ('127.0.0.1', 9999))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
main()