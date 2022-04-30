import socket

HEADER = 64      
PORT = 5050                       # this is the port number i.e the local address
FORMAT = "UTF-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER  = "192.168.43.71"         # this is the ip_address
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR) 

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT) 
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message) 

send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Tim!")

send(DISCONNECT_MESSAGE)