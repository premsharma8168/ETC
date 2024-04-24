import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address= (socket.gethostname(), 1234)
s.bind(address)
s.listen(5)

print(f'Server listening on {address}')

while True:
    s, addr = s.accept()
    print(f'Got connection from {addr}')
    secret_number = 54

    while True:
        guess = s.recv(1024).decode()

        if not guess:
            break

        guess = int(guess)

        if guess < secret_number:
            response = 'Higher'
        elif guess > secret_number:
            response = 'Lower'
        else:
            response = 'Correct!'


        s.send(response.encode())
    s.close()