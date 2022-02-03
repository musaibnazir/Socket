from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('127.0.0.1', 0))
# OS chooses port
print ("using", s.getsockname())
server = ('127.0.0.1', 11114)
packet = "client1 sending"
s.sendto(packet.encode(), server)
data, addr = s.recvfrom(1024)
s.close()
