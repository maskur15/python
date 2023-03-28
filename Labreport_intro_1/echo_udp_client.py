import socket
udp_ip_address="127.0.0.1"
udp_port_no=6789
while True:

    message = input("Enter echo : ")
    clientsocket= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    clientsocket.sendto(message.encode(),(udp_ip_address,udp_port_no))
    mes,address=clientsocket.recvfrom(1024)
    print(mes.decode())
