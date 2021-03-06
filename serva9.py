import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs



class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # sending an '200 ok' response
        self.send_response(200)

        #setting the header
        self.send_header("Content-type", "text/html")

        #whenever using 'send_header', you also have to call 'end_headers'
        self.end_headers()


        #Extracr query param
        name = 'World'
        query_components = parse_qs(urlparse(self.path).query)
        if 'name' in query_components:
            name = query_components["name"][0]

        #some custom HTML code , possibly generated by another function
        html = f"<html><head></head><body><h1> Hello {name}</h1></body>"


        #writing thhe HTML contents with UTF-8
        self.wfile.write(bytes(html, "utf8"))

        return
#create an object of the above class
handler_object = MyHttpRequestHandler
PORT = 8000
my_server = socketserver.TCPServer(("", PORT),  handler_object)

#start the server
my_server.serve_forever()
