import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 3000))

data = client_socket.recv(1024)

print('server:',data.decode())

client_socket.close()