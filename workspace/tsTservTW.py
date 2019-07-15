from twisted.internet import protocol, reactor
from time import ctime
import datetime

PORT = 21567


class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connect from: ', clnt)

    def dataReceived(self, data):
        # self.transport.write('[%S] %S' % (ctime(), data))

        # self.transport.write(ctime(), data)
        date_time = datetime.datetime.now().ctime()
        self.transport.write(date_time.encode('utf-8'))
        # self.transport.write(data)


factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()
