from itchat.requests.tu_ling import get_response as tu_ling_get_response
from itchat.requests.qing_yun_ke import get_response as qing_yun_ke_get_response
from itchat.requests.tu_ling_AI import get_response as tu_ling_AI_get_response
from mongo.connect import mongo_connect
import random

class Change(object):
    # 机器人可选集合
    robots = [0,1,2]
    # 数据库集合
    db = mongo_connect().connect_mongo('robot')

    def __init__(self, *args):
        super(Change, self).__init__(*args)        
        self.robot_id = self.db.find_one()['robotId']

    def qing_yun_ke(self,msg):
        result = qing_yun_ke_get_response(msg)
        if result.get('result') != 0:
           return self.auto_switch()
        else:   
            return result.get('content').replace("{br}", "\n")

    def tu_ling(self,msg):
        result = tu_ling_get_response(msg)
        if result['code']!=10000:
            return self.auto_switch()
        else:
            return result.get('text')

    def tu_ling_AI(self,msg):
        result = tu_ling_AI_get_response(msg)
        if result['code']!=10000:
            return self.auto_switch()
        else:
            text=''
            for item in result['data']['results']:
                print(item)
                text+=item['values']['text']
            return text
        
    def select_robot(self,robot_id):
        robots = {
            0:"qing_yun_ke",
            1:"tu_ling",
            2:"tu_ling_AI"
        }
        my_query = { "robotId": self.robot_id,"name":robots.get(self.robot_id) }
        new_values = { "$set": { "robotId": robot_id,"name":robots.get(robot_id)} }
        self.robot_id = robot_id
        self.db.update_one(my_query,new_values)
        return '换人啦～'
    
    def auto_switch(self):
        try:
            auto_robot_id = list(filter(lambda x: x != self.robot_id, self.robots))
            radom_index = random.randint(0,len(auto_robot_id)-1)
            self.select_robot(auto_robot_id[radom_index])
            return '切换成功'
        except:
            return '自动切换失败'

    def result_message(self,msg):
        if self.robot_id == 1:
            return self.qing_yun_ke(msg)
        elif self.robot_id == 0:
            return self.tu_ling(msg)
        elif self.robot_id == 2:
            return self.tu_ling_AI(msg)

            
        