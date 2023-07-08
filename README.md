# 投稿姬
把YouTube视频自动搬运到B站的机器人，依靠B站消息触发，也支持命令行调用。  

# 快速开始
```shell
sudo apt install git
sudo git clone https://github.com/yesmore/upbot.git
cd Violet
sudo bash setup.sh
./biliup login
```
在运行下面这行命令之前请先参照下文中"正经的使用方法"中的2，3步对task_manager.py 和 new_downloader.py 做出修改
```shell
sudo bash start.sh 
```
***

# 正经的使用方法 
1.使用biliup进行[命令行登陆](https://biliup.github.io/biliup-rs/index.html#windows-%E6%BC%94%E7%A4%BA)
2.将task_manager.py中的OWNER变量改为自己的uid.  
3.将new_downloader.py中的`OWNER_NAME`变量改为自己的用户名.  
4.运行
```shell
sudo bash setup.sh && sudo bash start.sh 
```

# 触发消息格式 
```
$<url>$
```
如:
```
$https://www.youtube.com/watch?v=gqmsj7W2VGc$
```
直接向机器人所登陆的账号私信发送即可</br>

# 命令行调用方式
```shell
python3 new_downloader.py <url> <tid>
```
如:
```shell
python3 new_downloader.py https://www.youtube.com/watch?v=xxxxxxxxx 21
```

> tid参考：https://biliup.github.io/tid-ref.html

# 示例demo

[盛佳冉](https://space.bilibili.com/486914885/video)
