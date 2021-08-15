#coding=utf8
import requests
import itchat

def get_response(msg):
    apis=[
        "8edce3ce905a4c1dbb965e6b35c3834d",
        "eb720a8970964f3f855d863d24406576",
        "1107d5601866433dba9599fac1bc0083",
        "71f28bf79c820df10d39b4074345ef8c",
        "ec3cff2c300048a2b11ed63c0180b3cd",
        "587f10e38dac47bd9abbaa7cfcf3dc64",
        "40d56dcf5e1d4edc8a891eb824a11437",
        "b2c05bbcc375412f8621e433648748fc",
        "233301805efc4e32a95c95bf5de7af4a",
        "e623e8acef674f36ad6ccd9b8f9934d3",
        "ea284a3fb5914c6498dcbf4eeb772aab",
        "9adec2d2c4fc4de4bb186c6e1e5119c8",
        "e8c190a005adc401867efd1ad2602f70",
        "ec3cff2c300048a2b11ed63c0180b3cd"
    ]

    KEY = '8edce3ce905a4c1dbb965e6b35c3834d'
    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key' : KEY,
        'info' : msg,
        'userid': 'wechat-robot',
    }
    print(data)
    try:
        r = requests.post(apiUrl, data=data).json()
        if r.get('code')!=10000:
            print(r)
            key_index = apis.index(KEY)
            print(key_index)
            if key_index == len(apis)-1:
                return { 'code':500 }
            else:
                KEY = apis[key_index+1]
                data['key'] = KEY
                print(data)
                res = requests.post(apiUrl, data=data).json()
                return res
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        
        else:    
            return r
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return