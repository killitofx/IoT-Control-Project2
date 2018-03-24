from wxpy import*
import requests
jurl = "http://192.168.10.11:8000/api/cn/"

bot=Bot()
my_friendall = bot.friends()    
@bot.register(my_friendall)
def auto_reply(msg):

    if '开' in msg.text:
        data = msg.text
        data = data.replace("开",'')
        r = requests.get(jurl + data +'/1')
        if r.status_code == 200:
            return "%s打开成功" % data
        elif r.status_code == 403:
            return "设备:%s处于打开状态" % data
        elif r.status_code == 404:
            return "无法找到设备:%s" % data
        else:
            return "请再试一次"

    if '关' in msg.text:
        data = msg.text
        data = data.replace('关','')
        r = requests.get(jurl + data + '/0')
        if r.status_code == 200:
            return "%s关闭成功" % data
        elif r.status_code == 403:
            return "设备:%s处于关闭状态" % data
        elif r.status_code == 404:
            return "无法找到设备:%s" % data
        else:
            return "请再试一次"

embed()
