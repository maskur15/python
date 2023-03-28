import socket
s=socket.socket()
s.settimeout(2)
host = input("please enter the address you want to scan : ")
port = int(input("Please enter the port you want to scan : "))
print(host)
def portScanner(port):
    print("The port is scanning.......")
    if s.connect_ex((host,port)):
        print("The port is closed")
    else:
        print("The port is open")
portScanner(port)