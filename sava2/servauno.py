import socket
import ssl
from handleRequests import handleRequests
import ssl
from envar import *


host, port = LOCALHOST_NAME,PORT_ADDRESS
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('/home/mykmyk/serva/sava2/keys/Demo.pem', '/home/mykmyk/serva/sava2/keys/Demo.key', password="mike")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.bind((host, port))
    my_socket.listen(1)
    
    print ("I am listening on :", port)
    
    with context.wrap_socket(my_socket, server_side=True) as serverSock:
        while True:
            connection, address = serverSock.accept()
            request = connection.recv(1024).decode('utf-8')
            print(request)
            handleThisRequest = handleRequests(request)
            connection.send(handleThisRequest.handler())
            connection.close()

"""
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.bind((HOST, PORT))
my_socket.listen(1)

print('Iam is listening on :', PORT)

while True:
    connection, address = my_socket.accept()
    request = connection.recv(1024).decode('utf-8')
    print(request)
    handleThisRequest = handleRequests(request)
    connection.send(handleThisRequest.handler())
    connection.close() 
"""    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
