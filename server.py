import socket
import sys
import time
#end of import statement#

# initialization#
s=socket.socket()
host=socket.gethostname()
print("server will start on host:",host)
port=1105
s.bind((host,port))
print("")
print("server done binding to host and port successfully")
print("")
print("server is waiting for incoming connections")
print("")
s.listen(1)
conn,addr = s.accept()
print(addr,"has connected to the server and is now online......")
print("")
message=input(str(">> "))
message=message.encode()
conn.send(message)
print("message has been sent...")
print("")
incoming_message = conn.recv(1024)
incoming_message = incoming_message.decode()
print("client:",incoming_message)
print("")

             
