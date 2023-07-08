import json
import time

import new_downloader
import requests

OWNER=486914885 #要发送命令的用户uid(现在B站叫mid)
REFERSH_TIME=2.5 #检查命令消息间隔时间，单位：分钟


def get_cookie():
    text=open("./cookies.json").read()
    json_obj=json.loads(str(text))
    cookie_list=json_obj["cookie_info"]["cookies"]
    i=0
    while True:
        if cookie_list[i]["name"]=="SESSDATA":
            SESSDATA=cookie_list[i]["value"]
            break
        i+=1
    return SESSDATA

def no_space(string):
    return string.replace(" ", "")

def get_bilibili_api(url):
    r = requests.get(url,cookies={"SESSDATA": get_cookie()})#,verify=False)
    return json.loads(r.text)

def save(data,path="./data.json"):
    with open(path, "w") as f:
        f.write(json.dumps(data))

def read(file_name="./data.json"):
    with open(file_name, "r") as f:
        return json.loads(f.read())

def match_url(url):
    urlStringList=url.split("$")
    return no_space(urlStringList[1])

def get_task_list():
    #global TID #顺便刷下TID
    return_list=[]
    task_list=get_bilibili_api("https://api.vc.bilibili.com/svr_sync/v1/svr_sync/fetch_session_msgs?talker_id="+str(OWNER)+"&session_type=1")["data"]["messages"]
    i=0
    while i<len(task_list):
        msg_obj=task_list[i]
        if msg_obj["sender_uid"]==OWNER and msg_obj["msg_type"]==1:#鉴权&&防止特殊消息混入
            if msg_obj["content"].find("$")!=-1:
                return_list.append(match_url(msg_obj["content"]))
            #if msg_obj["content"].find("<")!=-1 and msg_obj["content"].find(">")!=-1:
            #    TID=int(no_space(msg_obj["content"].split("<")[1].split(">")[0]))
            #    print("TID is updated to "+str(TID))
            #    save(TID,"./TID.json")
        i+=1
    return return_list


def main():
    try:
        task_history=read()
    except:
        task_history=[]#initial list task_history
    this_download=False#开始视为没请求过接口
    while True:
        task_list=get_task_list()
        n=0
        while n<len(task_list):
            task=task_list[n]
            if task not in task_history:
                print("new task: "+task)
                if task.find("*")!=-1:
                    plain=False
                else:
                    plain=True
                if task.find("<")!=-1:
                    TID = int(no_space(task.split("<")[1].split(">")[0]))
                else:
                    TID = 130 #默认TID misic
                new_downloader.main(task,TID,plain)
                task_history.append(task)
                save(task_history)
                this_download=True
            n+=1
        if not this_download:
            time.sleep(REFERSH_TIME*60)
        else:
            this_download=False

if __name__=="__main__":
#    try:
#        TID=int(read("./TID.json"))
#    except FileNotFoundError:
#        TID=21 #tid保护性赋值（别问我为什么是生活-日常，因为容易过审）
    while True:
        try:
            main()
        except Exception as e:
            print(e)
            time.sleep(REFERSH_TIME*60)
            continue
