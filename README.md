# IoT-Control-Project
这是一个远程控制系统，能远程控制设备，支持网页控制，微信控制，开放API。<br>
系统由php服务端，lua/python控制硬件执行指定操作，通用的json格式通信，支持定时控制<br>
硬件支持NodeMCU,Arduino,Raspberry,对三菱PLC的支持开发到一半（太混了，准备重写）<br>
最严重BUG为采用HTTP协议，服务器负载过重，无法大规模部署<br>
php部分重复函数过多，内容混乱，到后期我自己都看不懂了<br>
由于第一次写项目，内容过于混乱，存在很多BUG，遂决定重写，日期待定
