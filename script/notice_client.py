import socket
import json
ip_port = ('127.0.0.1', 8080)
sk = socket.socket()
sk.connect(ip_port)

data = {'id': 1}
inp = json.dumps(data)
data = sk.recv(1024)
print(data)

while True:
    sk.sendall(inp.encode())
    data = sk.recv(1024)
    data = data.decode()
    # data = json.loads(data)
    print(data)
    # if i ==3:
    #     sk.close()
    #     break
