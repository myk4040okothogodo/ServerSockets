from  http.server import BaseHTTPRequestHandler
import cgi
import webbrowser
tasklist = ['task 1', 'task 2', 'task e']
new =2

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):


        if self.path.endswith('/login'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            url ="/home/mykmyk/serva/sava/static/login.html"
            webbrowser.open(url, new=new)

        if self.path.endswith('/tasklist'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
                    

            output = ''
            output += '<html><body>'
            output +='<h1>Task list</h1>'
            output += '<h3><a href="/tasklist/new">Add New Task</a></h3>'
            for task in tasklist:
                output += task
                output += '<a href="/tasklist/%s?remove">X</a>' % task
                output += '</br>'
            output += '</body></html>'
            self.wfile.write(output.encode())

        if self.path.endswith('/new'):
           self.send_response(200)
           self.send_header('content-type', 'text/html')
           self.end_headers()

           output = ''
           output += '<html><body>'
           output += '<h1>Add New task</h1>'

           output += '<form method="POST" enctype="multipart/form-data" action="/tasklist/new">'
           output += '<input name="task" type="text" placeholder="Add new task">'
           output += '<input type="submit" value="Add">'
           output += '</form>'
           output += '</body></html>'
           self.wfile.write(output.encode())

        if self.path.endswith('/remove'):
            listIDPath = self.path.split('/')[2]
            print(listIDPath)
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output = ''
            output += '<html><body>'
            output += '<h1>Remove task: %s </h1>' % listIDPath.replace('%20', ' ') 
            output += '<form method= "POST" enctype="multipart/form-data" action="/tasklist/%s/remove">' % listIDPath
            output += '<input type="submit" value="Remove">'
            output += '</body></html>'
            self.wfile.write(output.encode())

    def do_POST(self):
        if self.path.endswith('/new'):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                new_task = fields.get('task')
                print(new_task)
                tasklist.append(new_task[0].decode("utf-8"))

            self.send_response(301)
            self.send_header('content-type', 'text/html')
            self.send_header('Location', '/tasklist')
            self.end_headers()
