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
        break

def file_recv():
    fname=client.recv(1024).decode()
    print(f'file is {fname}')
    file=open(r'C:\Users\Vatsal pc\Downloads\{name}'.format(name=fname),'wb')
    while True:
        line=client.recv(1024)
        file.write(line)
        if not line:
            print('file has been recieved in the Downloadsfolder')
            return 0

import socket
client=socket.socket()
client.connect(('192.168.0.10',1234))
print('Connected to server \n\n')
while True:
    cmsg = input("client-->")
    client.send(cmsg.encode())
    if cmsg.lower()=='sending file':
        file_send()
    if cmsg.lower()=='endofchat':
        print()
        client.close()
        break
    
    smsg=client.recv(1024).decode()
    print(f'server-->{smsg}'.rjust(60))
    if smsg.lower()=='sending file':
        file_recv()
    if smsg.lower()=='endofchat':
        print()
        client.close()
        break
        