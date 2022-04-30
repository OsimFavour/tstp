import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
# port number can be anything between 0-65535(we usually specify non-privileged ports which are > 1023)
s.listen(5)

while True:
    clt, adr = s.accept()
    print(f"Connection to {adr} established")
    # f string is literal string prefixed with f which
    # contains python expression inside braces

    clt.send(bytes("Socket Programming in Python", "utf-8"))
    # to send info into the client socket

    clt.close()