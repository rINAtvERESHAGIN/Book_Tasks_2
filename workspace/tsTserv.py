from socket import *

HOST = ''
PORT = 21569
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpServSock = socket(AF_INET, SOCK_STREAM)
tcpServSock.bind(ADDR)
tcpServSock.listen(5)

while True:
    print('waiting for connection')
    tcpCliSock, addr = tcpServSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print(data)
        # message = input('> ')
        message = data
        # tcpCliSock.send(message.encode('utf-8'))
        tcpCliSock.send(message)
    tcpCliSock.close()
tcpServSock.close()
