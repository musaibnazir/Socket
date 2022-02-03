import socket
from tkinter import messagebox as m
def a():
    s=socket.socket()
    portno = 10011
    print("Socket Established")
    s.bind(('',portno))
    s.listen()
    print("Listing")
    while True:
        c,addr=s.accept()
        print("connected")
        str="First Server Message"
        str1="Second Server Message"
        str2="Third Server Message"
        str3="Fourth Server Message"
        c.send(str.encode())
        c.send(str1.encode())
        c.send(str2.encode())
        c.send(str3.encode())
