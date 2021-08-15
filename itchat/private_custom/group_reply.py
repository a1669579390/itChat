import itchat

class Group():
    def group_msg(self,msg):
        if msg['isAt']:
            return u'@%s\u2005%s' % (msg['ActualNickName'],
            get_response(msg['Text']) or u'收到：' + msg['Text'])
