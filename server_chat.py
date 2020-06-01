def file_send():
    fname=input('Enter the name of the file: ').encode()
    client.send(fname)
    path=input('Enter the path of the file you want to send: ')
    file=open(path,"rb")
    while True:
        fdata=file.readlines()
        for line in fdata:
            client.send(line)
        print('file has been received\nServer is closing')
        return 0

def file_recv():
    fname=client.recv(1024).decode()
    print(f'file is {fname}')
    file=open(r'C:\Users\Vatsal pc\Downloads\{name}'.format(name=fname),'wb')
    while True:
        line=client.recv(1024)
        file.write(line)
        if not line:
            print('file has been recieved in the Downloadsfolder')
            break

import socket
server=socket.socket()
server.bind(('192.168.0.10',1234))
server.listen()
#print(f'server:{192.168.0.10:1234}'')
client,addr=server.accept()
print(f'\nClient: {addr[0]}:{addr[1]}')
while True:
    cmsg=client.recv(1024).decode()
    print(f'client-->{cmsg}'.rjust(60))
    if cmsg.lower()=='sending file':
            file_recv()
    if cmsg.lower()=='endofchat':
            print('Client has closed chat session')
            client.close()
            break
      
    smsg=input('server-->').encode()
    client.send(smsg)
    if smsg.decode().lower()=='sending file':
            file_send()
    if smsg.decode().lower()=='endofchat':
            print('server has closed chat session')
            client.close()
            break
server.close()