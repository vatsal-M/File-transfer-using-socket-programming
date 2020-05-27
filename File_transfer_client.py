import socket
import json
client=socket.socket()
client.connect(('192.168.0.10',2000))
print('Client is connected to server ip:192.168.0.10\n\n')
fname=client.recv(1024).decode()
file=open(f'Downloads\{fname}','wb')
while True:
    line='oo'
    while line!=1:
        line=client.recv(1024)
        json.dump(line,file)
    print('file has been recieved in the Downloads folder')
    client.close()
    break
file.close()

    