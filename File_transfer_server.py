import socket
server=socket.socket()
ip='192.168.0.10'
port=2000
server.bind((ip,port))
server.listen()
print(f'server made with ip:{ip} and port:{port}')
client,addr=server.accept()
print(f'\nClient: {addr[0]}:{addr[1]}')
fname=input('Enter the name of the file: ').encode()
client.send(fname)
path=input('Enter the path of the file you want to send: ')
file=open(path,"rb")
while True:
    fdata=file.readlines()
    for line in fdata:
        client.send(line)
    eof='1'.encode()
    client.send(eof)
    print('file has been received\nServer is closing')
    client.close()
    break
file.close()
server.close()