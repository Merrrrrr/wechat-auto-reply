import itchat
import requests


def get_response(msg):
    print(msg)  # 从好友发过来的消息
    api_url = 'http://www.tuling123.com/openapi/api'  # 图灵机器人网址
    data = {
        'key': '59eb12508f42411eb3f0addf067e2fe9',  # 如果这个 apiKey 如不能用，那就注册一次
        'info': msg,  # 这是我们从好友接收到的消息 然后转发给图灵机器人
        'userid': 'wechat-robot',  # 这里你想改什么都可以
    }
    r = requests.post(api_url, data=data).json()  # 把data数据发
    print(r.get('text'))  # 机器人回复给好友的消息
    return r


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    if msg['FromUserName'] == userName:
        return get_response(msg["Text"])["text"]


if __name__ == '__main__':
    itchat.auto_login()  # hotReload = True, 保持在线，下次运行代码可自动登录,可以添加enableCmdQR=True参数，让二维码显示到命令行上，另外部分系统可能字符宽度有出入，可以通过把enableCmdQR赋值为特定的倍数进行调整。如设置值为2
    users = itchat.search_friends(name='名字')
    userName = users[0]['UserName']
    itchat.run()
