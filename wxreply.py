#coding=utf8
import itchat
 
# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register('Text')



def text_reply(msg):
    # 当消息不是由自己发出的时候
    if  msg['FromUserName'] == userName:
        # 发送一条提示给文件助手
        #itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
        #                (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
        #                 msg['User']['NickName'],
        #                 msg['Text']), 'filehelper')
        # 回复给好友
        message = msg['Text']
        return message
 
if __name__ == '__main__':
    itchat.auto_login()
 
    # 获取自己的UserName
    #myUserName = itchat.get_friends(update=True)[0]["UserName"]
    users = itchat.search_friends(name='名字')
    userName = users[0]['UserName']
    itchat.run()