def file_send(client):
    fname=input('Enter the name of the file: ').encode()
    client.send(fname)
    path=input('Enter the path of the file you want to send: ')
    file=open(path,"rb")
    fdata=file.read(1024)
    while fdata:
        client.send(fdata)
        fdata=file.read(1024)
    print('file has been sent')
    return 0

def file_recv(client):
    fname=client.recv(1024).decode()
    print(f'file is {fname}')
    file=open(r'C:\Users\Vatsal pc\Downloads\{name}'.format(name=fname),'wb')
    recv_data=client.recv(1024)
    while recv_data:
        file.write(recv_data)
        recv_data=client.recv(1024)
    print('file has been received')
    return 0

import socket
client=socket.socket()
client.connect(('192.168.0.10',3000))
print('Connected to server \n\n')
while True:
    cmsg = input("client-->")
    client.send(cmsg.encode())
    if cmsg.lower()=='sending file':
        file_send(client)
    if cmsg.lower()=='endofchat':
        print()
        client.close()
        break
    
    smsg=client.recv(1024).decode()
    print(f'server-->{smsg}'.rjust(60))
    if smsg.lower()=='sending file':
        file_recv(client)
    if smsg.lower()=='endofchat':
        print()
        client.close()
        break
        