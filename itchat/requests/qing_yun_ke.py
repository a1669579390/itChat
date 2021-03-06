#coding=utf8
import requests
import itchat

# 青云客为备用机器人
def get_response(msg):
    apiUrl = 'http://api.qingyunke.com/api.php'
    data = {
        'key' : 'free',
        'msg' : msg,
        'appid' : '0',
    }
    print(data)
    try:
        r = requests.get(apiUrl, params=data).json()
        print(r)
        
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return