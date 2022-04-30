import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

server.connect((host, port))
server.send("I LOVE YOU".encode("utf-8"))
print(server.recv(1024).decode("utf-8"))
server.close()