from socket import *

HOST = '127.0.0.1'
PORT = 21569
BUFSIZ = 1024




print('enter host and port')
print('if not, use default')

while True:
    print('use default?: enter yes, no')
    answer = input('> ')
    if answer == 'yes':
        print('default')
        ADDR = (HOST, PORT)
        break
    elif answer == 'no':
        HOST = input('> ')
        print('HOST: ', HOST)
        PORT = input('> ')
        print(PORT)
        ADDR = (HOST, int(PORT))
        break
    else:
        print('enter yes or no')


tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data)

tcpCliSock.close()
