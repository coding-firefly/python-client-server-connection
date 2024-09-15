#sample code for reference
import socket

server = ""
port = ""
#placeholder for ip_address/server url and port

def get_data():
    data = input("message input\n->")
    return data

def message_try(server, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((server, int(port)))
        #connection to server based on input()
        parcel = 0
        #placeholder, anything as long its not "close"
        while parcel != "close":
        #keep running as long var parcel is not "close"
        #which it will send it as data to server once before self breaking
            parcel = input("parcel message:\n->")
            s.sendall(parcel.encode())
            #sending data after .encode()
        s.close()
    except:
        print("process_FAILED")

def get_input():
#just to get input for ip and port
    global server, port
    server = input("server or ip\n->")
    port = input("port\n->")

#process starter
get_input()
message_try(server, port)
