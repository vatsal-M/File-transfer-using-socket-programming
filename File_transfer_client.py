import socket
client=socket.socket()
client.connect(('192.168.0.10',2000))
print('Client is connected to server ip:192.168.0.10\n\n')
fname=client.recv(1024).decode()
print(f'file is {fname}')
file=open(r'C:\Users\Vatsal pc\Downloads\{name}'.format(name=fname),'wb')
while True:
    line=client.recv(1024)
    file.write(line)
    if line=='1':
        print('file has been recieved in the Downloadsfolder')
        client.close()
        break
file.close()

    