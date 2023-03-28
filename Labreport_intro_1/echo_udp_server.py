import  socket
udp_ip_address = "127.0.0.1"
udp_port_no=6789
serversocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serversocket.bind((udp_ip_address,udp_port_no))
while True:
    data,address=serversocket.recvfrom(1024)
    print("Send echo: ",data.decode())
    serversocket.sendto(data,address)