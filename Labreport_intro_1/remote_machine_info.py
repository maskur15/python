import  socket
def get_remote_machine_info():
    remote_host ='www.rmit.edu.au'
    try:
        print('Remote host name: %s'%remote_host)
        print('IP address: %s: '%socket.gethostbyname(remote_host))
    except socket.error as err_mess:
        print('Error accessing %s: error number and detail %s'%(remote_host,err_mess))
if __name__=="__main__":
    get_remote_machine_info()
