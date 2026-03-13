import socket


s = socket.socket()
port = 11177
s.connect(("127.0.0.1", port))

# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
s.close()