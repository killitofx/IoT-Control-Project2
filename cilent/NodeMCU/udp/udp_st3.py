import socket
import requests
import json
import time
import threading

url = 'http://192.168.10.11:8000/'

api_url = url + 'api/'
alive_url = url + 'alive/'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 9999))

def req(url,playload=0):
    if playload:
        kv = playload
        r = requests.get(url, params=kv)
    else:
        r = requests.get(url)
    return r.text



def udp_rec():
    print('start')
    while True:
        data, addr = s.recvfrom(1024)
        print(addr,data)
        #print('Received from %s:%s.' % addr,data)
        data = json.loads(data)
        if 'alive' in data['method']:
            ip_address = '%s:%s' % (addr[0], addr[1])
            kv = {'id': data['id'], 'ip':ip_address}
            req(alive_url + 'add', playload=kv)
            state = req(api_url + 'id/' + str(data['id']))
            state = json.loads(state)
            state = {"id": data['id'], "state": state['state'], "type": state['type']}
            state = json.dumps(state).encode()
            s.sendto(state, addr)
        elif "apply" in data['method']:
            device_id = str(data["id"])
            r = requests.get(alive_url + "active/" + device_id)


def check_data():
    while True:
        try:
            alive_data = req(alive_url + "get")
            alive_data = json.loads(alive_data)
            change_data = req(api_url + "gc/")
            change_data = json.loads(change_data)
            for i in change_data.values():
                if str(i) in alive_data.keys():
                    ip = alive_data[str(i)]
                    device_id = i
                    state_data = req(api_url + 'id/' + str(device_id))
                    state_data = json.loads(state_data)
                    state = {"id": state_data['id'], "state": state_data['state'], "type": state_data['type']}
                    state = json.dumps(state).encode()
                    ip = ip.split(':')
                    addr = (ip[0], int(ip[1]))
                    s.sendto(state, addr)
                    req(api_url + 'cgc/' + str(device_id))
                    req(alive_url + 'unactive/' + str(device_id))
                    print(state, addr)
        except:
            pass
        finally:
            time.sleep(1)




threads = []
t1 = threading.Thread(target=udp_rec)
threads.append(t1)
t2 = threading.Thread(target=check_data)
threads.append(t2)
def main():
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

main()