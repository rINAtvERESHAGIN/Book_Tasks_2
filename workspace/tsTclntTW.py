from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 21567


class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = input('> ')
        if data:
            print('...sending %s...' % data)
            recompil_data = data.encode('utf-8')
            self.transport.write(recompil_data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print(data)
        self.sendData()


class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()


reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()
