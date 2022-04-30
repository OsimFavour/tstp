import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get name out of local machine
hostname = socket.gethostname()

# set port
port = 8888

# connecting to our hostname at port 8888
server.connect((hostname, port))

server.send(f"THANK YOU!".encode("utf-8"))

msg = server.recv(1024).decode("utf-8")
server.close()

# print the message we received
print("{}".format(msg))
# print(f"{msg}")