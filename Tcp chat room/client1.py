import  socket
client = socket.socket()
client.connect(('localhost',34443))
mess=client.recv(1024)
print(mess.decode())
client.send("Hi this is new client".encode())