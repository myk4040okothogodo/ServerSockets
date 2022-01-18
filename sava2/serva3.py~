import socket
HOST, PORT = '127.0.0.1', 8082

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.bind((HOST, PORT))
my_socket.listen(1)


while True:
    connection, address = my_socket.accept()
    request = connection.recv(1024).decode('utf-8')
    string_list = request.split(' ')
    method = string_list[0] #first string is a method
    print(method)
    
    requesting_file = string_list[1] #second sstring is request
    print('Client request', requesting_file)
    myfile = requesting_file.split('?')[0] # after the '?' symbol
    print(myfile)
    
    myfile = myfile.lstrip('/')
    if(myfile == '/'):
        myfile = 'index.html'
        
        try:
            file = open(myfile, 'rb')
            response = file.read()
            file.close()
            
            
            header = 'HTTP/1.1 200 OK\n'
            if (myfile.endswith(".jpg")):
                mimetype = 'image/jpg'
            elif (myfile.endswith(".css")):
                mimetype  = 'text/css'
            else:
                mimetype = 'text/html'
            header += 'Content- Type: '+ str(mimetype)+'<strong>\n\n</strong>'
            final_response = header.encode('utf-8')
            final_response += response
            connection.send(final_response)
            connection.close()
        except Exception as e:
            header = 'HTTP/1.1 404 Not Found\n\n'
            response = '<html><body><center><h3>Error 404: File not found</h3><p>God Serva</p></center></body></html>'.encode('utf-8')
            final_response = header.encode('utf-8')
            final_response += response
            connection.send(final_response)
            connection.close()
                                       
