import socket

'''
连接建立后，服务器首先发一条欢迎消息，然后等待客户端数据，并加上Hello再发送给客户端。如果客户端发送了exit字符串，就直接关闭连接。
要测试这个服务器程序，我们还需要编写一个客户端程序：
'''

s_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#  建立连接：
s_client.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s_client.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s_client.send(data)
    print(s_client.recv(1024).decode('utf-8'))
s_client.send(b'exit')
s_client.close()
