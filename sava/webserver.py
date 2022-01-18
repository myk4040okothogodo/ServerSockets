from http.server import HTTPServer
from requesthandler import requestHandler
import ssl
import * from variables
import socket
import datetime 
import time



def main():
    port= PORT_ADDRESS
    localhost = LOCALHOST_NAME
    serverSocket = socket.socket()
    server = serverSocket.bind((localhost, port ));
    server.listen();
    print ('God is listening on  port %s ' %PORT)
    
    while(True):
        #keep acceptin connections from clients
        (clientConnection, clientAddress) = server.accept();
        secureClientSocket = ssl.wrap_socket(clientConnection, 
                                             server_side=True,
                                             ca_certs = "./DemoCA.pem",
                                             csrtfile = "./DemoSvr.crt",
                                             keyfile = "./DemoSvr.key",
                                             cert_reqs = ssl.CERT_REQUIRED,
                                             ssl_version = ssl.PROTOCOL_TLSv1_2
                                             );
        #Get certificcate from the client
        client_cert = secureClientSocket.getpeercert();
        clt_subject = dict(item[0] for item in client_cert['subject']);
        clt_commonName = clt_subject['commonName'];
        # check the client certifcate bears the exepected name as per severs' policy
        if not client_cert:
            raise Exception("Unaable to get certifcate from the clinet");
        if clt_commonName != 'Democlt':
            raise Exception("Incorrect coomon name in client certificate");
        # check time validity of the clients certificate
        t1 = ssl.cert_time_to seconds(client_cert['notBefore']);
        t2 = ssl.cert_time_to_seconds(client_cert['notAfter']);                                             
        ts time.time();
        if ts < t1:
            raise Exception("Client certificate not yet active")
        if ts > t2:
            raise Exception("Client certificate not yet active")
        # send current server time to the client
        serverTimeNow = "%s" %datetime.datetime.now();
        secureClientSocket.send(serverTimeNow.encode());
        print ("securely sent %s to %s"(serverTimeNow, clientAddress));
        # close the connection to the client
       

if __name__ == "__main__":
    main()
