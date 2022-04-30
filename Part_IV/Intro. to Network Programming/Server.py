import socket
import datetime

today = datetime.datetime.today()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # socket.SOCK_STERAM - streaming data through the sockets
# hostname = socket.gethostname()

port = 8888
server.bind(("", port))
server.listen(5)

while True:
    connect, address = server.accept()
    resp = connect.recv(1024).decode("utf-8")
    print(f"Message Noted! {resp}")
    connect.send(f"Received http requests on channel {address} {today}".encode("utf-8"))
    print(f"Message received on {today}")
    connect.close()