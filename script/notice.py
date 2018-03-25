import socketserver
import json
import requests
import time

get_url = "http://192.168.10.30:8000/api/id/"

class myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall(b"link ok")
        data = conn.recv(1024)
        data = data.decode()
        data = json.loads(data)
        ostate = -1
        while True:
            try:
                i = data["id"]
                r = requests.get(get_url + str(i))
                dev = json.loads(r.text)
                name = dev['name']
                state = dev['state']
                if not ostate == state:
                    if int(state):
                        txt = "设备 %s 开启 " % name
                        ostate = state
                    else:
                        txt = "设备 %s 关闭" % name
                        ostate = state
                    txt = txt.encode()
                    conn.sendall(txt)
                time.sleep(2)
            except:
                pass



if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), myserver)
    server.serve_forever()
