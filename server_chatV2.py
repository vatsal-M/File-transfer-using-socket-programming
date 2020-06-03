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
server=socket.socket()
server.bind(('192.168.0.10',3000))
server.listen()
client,addr=server.accept()
print(f'\nClient: {addr[0]}:{addr[1]}')
while True:
    cmsg=client.recv(1024).decode()
    print(f'client-->{cmsg}'.rjust(60))
    if cmsg.lower()=='sending file':
            file_recv(client)
    if cmsg.lower()=='endofchat':
            print('Client has closed chat session')
            client.close()
            break
      
    smsg=input('server-->').encode()
    client.send(smsg)
    if smsg.decode().lower()=='sending file':
            file_send(client)
    if smsg.decode().lower()=='endofchat':
            print('server has closed chat session')
            client.close()
            break
server.close()