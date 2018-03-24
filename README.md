# IoT-Control-Project 2 
一代系统由于某些原因已经无法使用了，当时还没开始用Git，感觉自己巨亏啊，浪费了半个暑假边学边写，心疼自己一秒钟。最近正好在学Django，正好拿来试试水。由于一代使用了一大堆语言，看起来比较混乱，就把二带单独拉出来了。  
2代完全抛弃了PHP，LUA，SQL，<del>JavaScript，Html，css</del>  这个不知道以后会不会用，暂时全是python

支持的设备
====
服务端：windows10，树莓派上都可以运行 亲测可用  
客户端：NodeMcu（micropython固件）树莓派上都可以运行  
扩展设备：三菱PLC ,arduino 这个都是通过树莓派转接，理论上可行，实际成功过一次，支持的话看心情  
微信远程控制：这个暂时支持，不知道以后会怎么样  
小娜：可以用语音控制
部署  
====
服务端
-------
1.安装python3.x，添加环境变量  
2.安装django框架2.0.x  
``` pip install django ```  
或者  
```pip3 install django ```  
3.复制server文件夹下的iot到任意文件夹，进入到有```manage.py``` 的文件夹下，打开```powershell/cmd/Terminal```,运行  
```python manage.py runserver 0.0.0.0:8000```  
服务顺利启动 建议服务端使用固定ip，防止应为ip变动造成的设备无法使用  
4.添加设备 进入django网址后（设备ip+：8000/admin）进入```Ports```，添加设备名称，设备形式（0为输出，1为读取端口数据并送回）设置端口状态（1/0），```is_change``` 打上勾，选择创建者后保存即可  
5.添加定时器（可选）进入```Times```表，点击增加，```ctrl```打上勾表示运行，```loop```打上勾表示启动循环，若不打勾，运行结束后会自动删除。```port_id```为添加设备的id号，```s_time```为开始时间，```c_time```为关闭时间 ```is_change```不要打勾，保存后定时器就创建完毕了。  
6.开启定时器依靠外部文件来刷新，所以要启动script文件夹中的```flash_time_list.py```文件来刷新。
微控制器 NodeMCU  
-------
使用 [nodemcu-flasher](https://github.com/nodemcu/nodemcu-flasher) 刷入NodeMCU下bin文件夹的文件  
使用 [uPyLoader](https://github.com/BetaRavener/uPyLoader) 由于没有打包，所以需要安装运行库  
```pip install PyQt5```   
```pip install pyserial>=3.1.1```
之后cmd cd到main.py 所在目录 运行  
``` python main.py```  
打开uPyLoader 之后根据提示 连接开发板 File—>init 初始化  
把Client-NodeMCU-http-```http4.py``` 扔到uPyloader的目录下，点击Transfer，文件就上传到设备了。同时打开boot文件，在boot文件中添加  
``` import http4```
来让NodeMCU上电自动运行  
修改```http4.py``` ```device_id_1 = 1``` 表示设备的一号端口对应数据库```Ports```表中id=1的设备，若不使用该端口，则 =0 **一号端口不能为=0**  
修改url 根据服务器地址修改服务器的ip地址和端口，保存之后设备就能读取数据库了  
  
udp版本只能工作在type0状态，尚且不稳定，故不推荐使用
微信  
-------
安装python [wxpy库](https://github.com/youfou/wxpy)  
``` pip install wxpy```  
或者从豆瓣镜像下载  
```pip install -U wxpy -i "https://pypi.doubanio.com/simple/"```  
修改wxts.py中的url为服务端地址 启动扫码登陆后向该微信号发送设备名称加开/关关键字就能顺利控制设备
PC  
-------
找个地方放pc.exe，创建快捷方式，在后面添加参数 ```-u 地址``` ```-i id``` ```-s state```  
```-u``` 不填时，默认```http://192.168.10.30:8080/api/cn```  
```-i``` 不填时，默认```id=1```  
```-s``` 不填时，默认```state=1```  
需要打开id=1的灯是 参数为 ```pc.exe -s 1```  
需要打开id=1的灯是 参数为 ```pc.exe -s 0```
创建完成后把快捷方式扔到  
``` C:\Users\用户名\AppData\Roaming\Microsoft\Windows\Start Menu\Programs ```  
并重命名 打开你好小娜，设备就可以语音启动了 
例如 快捷方式为 ```shutdown.exe -p``` 重命名为自毁程序 只要对小娜说```你好小娜，启动自毁程序```设备就关机了
...




