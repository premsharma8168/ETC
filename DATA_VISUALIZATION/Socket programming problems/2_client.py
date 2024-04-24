import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address= (socket.gethostname(), 1234)
s.connect((address))

while True:
    guess = input("Enter your guess (or 'q' to quit): ")

    if guess.lower() == 'q':
        break

    s.send(guess.encode())
    response = s.recv(1024).decode()

    if response == 'Correct!':
        print(response)
        break
    else:
        print(response)

s.close()