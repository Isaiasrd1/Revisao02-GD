#!/usr/bin/env python3

import socket

Host = '127.0.0.1'
Port = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host, Port))
filename= str(input('Arquivo > '))
s.sendall(filename.encode())

with open(filename, 'wb') as file:
    while 1:
        data = s.recv(4096)
        if not data:
            break
        file.write(data)

print('Arquivo recebido!')
# my_bytes = b"assim?"
# s.send(my_bytes)
# print('Mensagem: ', data.decode())


