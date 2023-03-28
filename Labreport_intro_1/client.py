import  socket
c = socket.socket()
c.connect(('localhost',8888))
while True:
    name = input("I : ")
    c.send(bytes(name,'utf-8'))
    print(c.recv(1024).decode())