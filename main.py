
import itchat
from itchat.components.change_robot import Change
from itchat.private_custom.group_reply import Group




@itchat.msg_register('Text')
def reply(msg):
    if msg['Text'] == "切换机器人":
        reply = Change().auto_switch()
    else:
        defaultReply = 'I received: ' + msg['Text']
        reply = Change().result_message(msg['Text'])
        
    return reply or defaultReply


@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def atta_reply(msg):
    return ({ 'Picture': u'图片', 'Recording': u'录音',
        'Attachment': u'附件', 'Video': u'视频', }.get(msg['Type']) +
        u'已下载到本地') # download function is: msg['Text'](msg['FileName'])

@itchat.msg_register(['Map', 'Card', 'Note', 'Sharing'])
def mm_reply(msg):
    if msg['Type'] == 'Map':
        return u'收到位置分享'
    elif msg['Type'] == 'Sharing':
        return u'收到分享' + msg['Text']
    elif msg['Type'] == 'Note':
        return u'收到：' + msg['Text']
    elif msg['Type'] == 'Card':
        return u'收到好友信息：' + msg['Text']['Alias']

@itchat.msg_register('Text', isGroupChat = True)
def group_reply(msg):
    print(msg)
    Group().group_msg(msg)

@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg(u'项目主页：github.com/littlecodersh/ItChat\n'
        + u'源代码  ：回复源代码\n' + u'图片获取：回复获取图片\n'
        + u'欢迎Star我的项目关注更新！', msg['RecommendInfo']['UserName'])

# itchat.auto_login(True, enableCmdQR=True)
itchat.auto_login(True, enableCmdQR=2)
itchat.run()