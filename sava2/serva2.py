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
    
    method = string_list[0]  #first string is a method
    print(method)
    requesting_file = string_list[1] #second string is request
    print('Client request', requesting_file)
    connection.close()
    
