#建立MongoDB数据库连接
from pymongo import MongoClient
import configparser
import os
 

class mongo_connect():

    def __init__(self):
        conf = configparser.ConfigParser()
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        conf.read(root_path + '/mongo/config.conf')  # 文件路径
        self.host = conf.get("mongo", "host")
        self.user = conf.get("mongo", "user")
        self.password = conf.get("mongo", "password")
        self.port = int(conf.get("mongo", "port"))
        self.database = conf.get("mongo", "database")

        

    def connect_mongo(self,new_collection):
        client = MongoClient(self.host,self.port)
        db = client.admin    # 先连接系统默认数据库admin
        db.authenticate(self.user, self.password) 
        db = client[self.database]
        collection = db[new_collection]
        return collection