from socket import *

HOST = gethostbyname(gethostname())

s = socket(AF_INET, SOCK_RAW, IPPROTO_IP)
s.bind(HOST, 0)

s.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)

s.ioctl(SIO_RCVALL, RCVALL_ON)

print(s.recvfrom(65565))

s.ioctl(SIO_RCVALL, RCVALL_OFF)

