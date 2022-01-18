from pageview import *

class router:
    def __init__(self, request):
        self.string_list = request.split(' ') #split request using space
        self.method = self.string_list[0]
        self.requesting_file = self.string_list[1]
        print("Client request: ",  self.requesting_file)
        self.myfile1 = self.requesting_file.split('?')[0]
        self.myfile = self.myfile1.lstrip('/')
        
    def routing(self):
        if self.method == "GET":
            if self.myfile == "":
                viewHome()
                
            elif self.myfile == "register":
                registrationView()
                
            elif self.myfile == "login":
                loginView()
                
            else:
                errorView()            
            
        # handle post method    
                              
                         
                           
        
