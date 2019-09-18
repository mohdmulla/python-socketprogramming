import socket
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
s.listen(1)
print(host)
print("waiting for incoming connection...")
conn ,addr = s.accept()
print(addr,"has connected successfully!")

#Tramsfer File
filename = input(str("Enter Filename:"))
file = open(filename,'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data has been Transmitted Successfully!")

