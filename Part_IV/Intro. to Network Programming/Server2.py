import socket                                               # Import Socket Module

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
host = socket.gethostname()                                 # Get local machine name
port = 12345                                                # Reserve a port for your service.
server.bind((host, port))                                   # Bind to the port

server.listen(5)                                            # Now wait for client connection
while True:
    connection, addr = server.accept()                               # Establish connection with clients
    print("Got connection from", addr)
    message = connection.recv(1024).decode("utf-8")
    print(f"Message received! {message}")
    connection.send(f"Thank you for connecting".encode("utf-8"))
    connection.close()                                               # Close the connection