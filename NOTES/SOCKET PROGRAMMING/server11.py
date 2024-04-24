import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 3000))

server_socket.listen(1)
print('waiting for connection........')
client, address = server_socket.accept()
print('Connected to address', address)
server_socket.send('welcome prem narayan'.encode())
# client.send('gla okh')
# client.close()
server_socket.close()