import socket
s = socket.socket()
host = input(str("Please enter the addresss of sender:"))
port = 8080
s.connect((host,port))
print("connected")

## Recieve File
filename = input(str("Enter Filename for incoming File:"))
file = open(filename,'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("File Transferred Successfully!")