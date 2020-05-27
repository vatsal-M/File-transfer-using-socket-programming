import socket
import json
server=socket.socket()
ip='192.168.0.10'
port=2000
server.bind((ip,port))
server.listen()
print(f'server made with ip:{ip} and port:{port}')
client,addr=server.accept()
print(f'\nClient: {addr[0]}:{addr[1]}')
path=input('Enter the path of the file you want to send: ')
file=open(path,"rb")
fname=input('Enter the name of the file: ').encode()
client.send(fname)
while True:
    fdata=json.load(file)
    for line in fdata:
        client.send(line)
    client.send(json.load(1))
    print('file has been received\nServer is closing')
    client.close()
    break
file.close()
server.close()