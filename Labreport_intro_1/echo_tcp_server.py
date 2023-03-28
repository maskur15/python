#echo server
import socket
server = socket.socket()
server.bind(('localhost',23423))
server.listen()
con,address=server.accept()
while True:
    mes=con.recv(1024).decode()
    if not mes: break
    print(mes)
    con.send(mes.encode())
con.close()