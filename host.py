import socket
import sys

server = "localhost"
port = 50007
#kindly key in own ip or localhost, port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
    #socket ip port binding
except:
    print("socket_FAILED")
    sys.exit()
  
s.listen(1)
#listen network with 1 queue
conn, address = s.accept()
ip, port = str(address[0]), str(address[1])

while True:
    data = conn.recv(1024)
    #accepting 1024 bytes of data
    print(data.decode())
    #readable output
    if str(data.decode()) == "close":
    #break when recieved a "close" string from client
    #will first close the host connection, then client
        print("close()_Triggered)
        break

 s.close()
