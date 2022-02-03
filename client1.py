import socket
from tkinter import messagebox as m
def client1():
    s = socket.socket()
    s.connect(('localhost',10011))
    print('Connected to Server')
    while True:
        msg=s.recv(1024)
        msg1=s.recv(1024)
        msg2=s.recv(1024)
        msg3=s.recv(1024)
        print(msg)
        print(msg1)
        print(msg2)
        print(msg3)
    s.close()
