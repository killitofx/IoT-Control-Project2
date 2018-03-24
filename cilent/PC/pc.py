import sys
import requests
ip = 'http://192.168.10.30:8000/api/cn/'
device_id = '1'
state = '1'
if sys.argv.count('-u'):
    num = sys.argv.index('-u')
    ip = sys.argv[num + 1]
if sys.argv.count('-i'):
    num = sys.argv.index('-i')
    device_id = sys.argv[num + 1]
if sys.argv.count('-s'):
    num = sys.argv.index('-s')
    state = sys.argv[num + 1]
url = ip + device_id + '/' + state
print('正在解析神秘代码 %s ' % url)
r = requests.get(url)