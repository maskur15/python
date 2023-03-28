#echo client
import socket
client = socket.socket()
client.connect(('localhost',23423))
while True:
    mess = input("Enter your echo: ")
    client.send(mess.encode())
    mess=client.recv(1024).decode()
    print(mess)