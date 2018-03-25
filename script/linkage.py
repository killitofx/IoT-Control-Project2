import requests
import json
import time
##设置联动对象 key 指向 value
# key跟随value变化
check_id = {"1": 3}
url = "http://192.168.10.30:8000/api/id/"
change_url = "http://192.168.10.30:8000/api/cn/"

def check_change(dev_id):
    dev_id = str(dev_id)
    r = requests.get(url + dev_id)
    data = r.text
    data = json.loads(data)
    state = data['state']
    return state

def apply_state(dev_id, state):
    state = str(state)
    dev_id = str(dev_id)
    r = requests.get(change_url + dev_id + '/' +state)

def main():
    while True:
        try:
            for i in check_id.keys():   #i为指向对象
                link = check_id[str(i)] #link为被指向对象
                state = check_change(link)
                ##可在此自定义if函数添加更丰富的规则
                #
                #
                apply_state(i, state)
        except:pass
        finally:time.sleep(1)
main()