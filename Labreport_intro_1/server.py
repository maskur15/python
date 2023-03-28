import socket
s = socket.socket()
print("socket created")
s.bind(('localhost',8888))
s.listen(3)
print('waiting for connection')
c, addr = s.accept()
while True:
    print("Connected with",addr)
    message= (c.recv(1024).decode())
    print(message)
    messtosend=input("I : ")
    c.send(bytes(messtosend,'utf-8'))
c.close()
