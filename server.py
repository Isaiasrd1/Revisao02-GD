#!/usr/bin/env python3

import socket
Host = 'localhost'
Port = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((Host, Port))
s.listen()
print('Aguardando conexão do cliente')
conn, ender = s.accept()
print('Conectado em: ', ender)

filename = conn.recv(4096).decode()
print('Arquivo enviado!')

with open(filename, 'rb') as file:
       for data in file.readlines():
            conn.send(data)
