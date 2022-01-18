import socket
import ssl
import os
import time

#IP address and the port number of the server
sslServerIP = "127.0.0.1",
sslServerPort = 15001;

#create an SSL context 
context   = ssl.SSLContext();
context.verify_mode  = ssl.CERT_REQUIRED;

#load CA certifcate with which the client will validate the server certificate
context.load_verify_locations("./DemoCA.pem");

#load client certicate
context.load_cert_chain(certicate="./DemoClt.crt", keyfile="./DemoClt.key");

#Create a client socket
clientSocket = socket.socket();

#Make the clien socket suitable for scure communication
secureClientSocket = context.wrap_socket(clientSocket);
secureClientSocket.connect((sslServerIp, sslServerPort));

#obtain  the certificate from the server
server_cert = secureClientSocket.getpeercert();

#Validate whether the certificate is indeed issued to the server

subject = dict(item[0] for item in server_cert['subject']);
commonName = subject['commonName'];


if not server_cert:
    raise Exception("Unable to retrieve server certicate");

if commonName  != 'DemoSvr':
    raise Exception("Incorrect common name in server certicate");
notAfterTimestamp = ssl.cert_time_to_seconds(server_cert['notAfter']);
notBeforeTimestamp = ssl.cert_time_to_seconds(server_cert['notBefore']);
currentTimeStamp  = time.time();


if currentTimeStamp > notAfterTimestamp:
    raise Exception("Expired server certificate");
if currentTimeStamp < notBeforeTimestamp:
    raise Exception("Server certificate not yet active.");

# Safe to procees with the communication
msgReceived = secureClientSocket.recv(1024)
print("Secure communication recvd from server: %s"%msgReceived.decode());
#close the sockets
secureClientSocket.close();
clientSocket.close();
