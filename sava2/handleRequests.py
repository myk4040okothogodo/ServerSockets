

class handleRequests:
    def __init__(self, request):
        #print(request)
        self.string_list = request.split(' ') #split request using spaces
        self.method = self.string_list[0]
        #print(self.method)
        self.requesting_file = self.string_list[1]
        print("Client request:", self.requesting_file)
        self.myfile1 = self.requesting_file.split('?')[0] #After the '?' symbol
        self.myfile = self.myfile1.lstrip('/')
    def handler(self):
        if self.method == "GET":  
            if (self.myfile == ""):
                myfile = "static/index.html"
            try:
                file = open(myfile, 'rb') # open file, r => read
                response = file.read()
                file.close()
            
                header = 'HTTP/1.1 200 OK\n'
                if (myfile.endswith(".jpg")):
                    mimetype = "image/jpg"
                elif (myfile.endswith(".css")):
                    mimetype = "text/css"
                else: 
                    mimetype = "text/html"
                    header += 'Content-Type: '+str(mimetype)+ '\n\n'
            except Exception as e:
                header = 'HTTP/1.1 404 Not Found\n\n'
                response = 'static/404.html'.encode('utf-8')
                    
            final_response = header.encode('utf-8')
            final_response += response 
            #return final_response
            if (self.myfile == "register"):
                myfile = "static/register.html"
            try:
                file = open(myfile, 'rb') # open file, r => read
                response = file.read()
                file.close()
            
                header = 'HTTP/1.1 200 OK\n'
                if (myfile.endswith(".jpg")):
                    mimetype = "image/jpg"
                elif (myfile.endswith(".css")):
                    mimetype = "text/css"
                else: 
                    mimetype = "text/html"
                    header += 'Content-Type: '+str(mimetype)+ '\n\n'
            except Exception as e:
                header = 'HTTP/1.1 404 Not Found\n\n'
                response = 'static/404.html'.encode('utf-8')
                    
            final_response = header.encode('utf-8')
            final_response += response 
            return final_response
               
            """  
            elif (self.myfile == "login"):
                myfile = "static/login.html"
                try:
                    file = open(myfile, 'rb') # open file, r => read
                    response = file.read()
                    file.close()
            
                    header = 'HTTP/1.1 200 OK\n'
                    if (myfile.endswith(".jpg")):
                        mimetype = "image/jpg"
                    elif (myfile.endswith(".css")):
                        mimetype = "text/css"
                    else: 
                        mimetype = "text/html"
                    header += 'Content-Type: '+str(mimetype)+ '\n\n'
                except Exception as e:
                    header = 'HTTP/1.1 404 Not Found\n\n'
                    response = '404.html'.encode('utf-8')
            
               
            elif (self.myfile=="register"):
                myfile = "static/register.html"
            try:
                file = open(myfile, 'rb') # open file, r => read
                response = file.read()
                file.close()
            
                header = 'HTTP/1.1 200 OK\n'
                if (myfile.endswith(".jpg")):
                    mimetype = "image/jpg"
                elif (myfile.endswith(".css")):
                    mimetype = "text/css"
                else: 
                    mimetype = "text/html"
                header += 'Content-Type: '+str(mimetype)+ '\n\n'
            except Exception as e:
                header = 'HTTP/1.1 404 Not Found\n\n'
                response = 'static/404.html'.encode('utf-8')
           
                
            else (self.myfile=="home"):
                myfile = "static/home.html"
            try:
                file = open(myfile, 'rb') # open file, r => read
                response = file.read()
                file.close()
            
                header = 'HTTP/1.1 200 OK\n'
                if (myfile.endswith(".jpg")):
                    mimetype = "image/jpg"
                elif (myfile.endswith(".css")):
                    mimetype = "text/css"
                else: 
                    mimetype = "text/html"
                header += 'Content-Type: '+str(mimetype)+ '\n\n'
            except Exception as e:
                header = 'HTTP/1.1 404 Not Found\n\n'
                response = 'static/404.html'.encode('utf-8')             
            """           
                
        
            
  
            
