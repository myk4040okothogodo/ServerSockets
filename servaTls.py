import ssl
import socket
import datetime
import time

ipAddress = "127.0.0.1";
port  = 15001;

#create a server socket
serverSocket = socket.socket();
serverSocket.bind((ipAddress, port));

#listen for incoming connections
serverSocket.listen();
print("Server listen:");
while (True):
    #keeep accepting connections from clients
    (clientConnection, clientAddress) = serverSocket.accept();

    #make the socket connection to the clients secure through SSLSocket
    secureClientSocket = ssl.wrap_socket(clientConnection, 
                                        server_side = True,
                                        ca_certs = "./DemoCA.pem",
                                        certfile = "./DemoSvr.crt",
                                        keyfile ="./DemoSvr.key",
                                        cert_reqs = ssl.CERT_REQUIRED,
                                        ssl_version = ssl.PROTOCOL_TLSv1_2);

    # Get certificate from the client
    client_cert = secureClientSocket.getpeercert();
    clt_subject = dict(item[0] for item in client_cert['subject']);
    clt_commonName = clt_subject['commonName'];

    #check the clients certificate bears the expected name as per servers policy
    if not client_cert:
        raise Exception("Unable to get the certficate from the client.");
    if clt_commonName != 'DemoClt':
        raise Exception("Incorrect common name in client certificate")

    #check time validity of the client certficate
    t1 = ssl.cert_time_to_seconds(client_cert['notBefore']);
    t2 = ssl.cert_time_to_seconds(client_cert['notAfter']);
    ts = time.time();

    if ts < t1:
        raise Exception("Client certificate not yet active");
    if ts > t2:
        raise Exception("Expired client certficate")
    #send current server time to the clinet
    serverTimeNow = "%s"%datetime.datetime.now();
    secureClientSocket.send(serverTimeNow.encode());
    print("securely sent %s to %s" %(serverTimeNow, clientAddress));

    #close the connection to the client
    secureClientSocket.close();
