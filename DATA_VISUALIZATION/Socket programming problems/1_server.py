# question---1
import socket
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
# address = ('localhost', 1234)
address= (socket.gethostname(), 1234)
s.bind(address)
s.listen(1)
print('Waiting for connnections.....address', address)
while 1:
    client, addr = s.accept()
    print('connection estaiblished', addr)
    data = client.recv(1024)
    # if not data:
    #     s.close()
    #     break
    print('Client:', data)
    client.send(data)
    print('Echo send')
    client.close()