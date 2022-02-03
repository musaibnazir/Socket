from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('127.0.0.1', 11114))
s.listen()
print("listining....")
while True:
    data, addr = s.recvfrom(1024)
    print ("Connection from", addr)
    s.sendto(data.upper(), addr)
    print ("received", data, "from", addr)
s.close()
