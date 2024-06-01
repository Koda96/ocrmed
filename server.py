from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
from filetransfer import FileUploadHandler

#Only for default inputs if user doesn't want to specify port or ip            
def defaultInput( prompt, default ):
    x = input(prompt)
    if not x.strip():
        x = default
    return x

class Server:
    def __init__(self, port = None, ip=None):
        self.ip = ip
        self.port = port
        self.f = False     

    def run(self):
        server_class = HTTPServer
        handler_class = FileUploadHandler
        server_address = (self.ip if self.ip else '', self.port)  # If ip is specified, uses it, if not, it listens to all ips on that specific port
        httpd = server_class(server_address, handler_class)
        httpd.serve_forever()
        
    def makedir(self, name):
        os.makedirs(name, exist_ok=True)
        print('Path {} created succesfully!'.format(name))
    
    def start(self):
        try:
            try:
                defaultIp = "127.0.0.1"
                defaultPort = "8000"
                self.ip = str(defaultInput("Specify server ip, press enter for default (localhost)\n", defaultIp))
                self.port = int(defaultInput("Specify server port to listen to, press enter for default (8000)\n", defaultPort))
            except TypeError:
                print("A port and ip number is needed to run the server, please make sure to use only integers on port or string on ip")
            except EOFError:
                print("Port or ip number can't be blank")
            else:
                print("Server succesfully started on port {}".format(self.port))
                self.makedir("uploads")
                self.setHTMLport(self.ip + ':' + str(self.port))
                self.run()
        except KeyboardInterrupt:
                print("Server stopped succesfully from KeyboardInterrupt")
        finally:
                self.setHTMLport("{url}")
                print("Server stopped listening to port {}".format(self.port))
              
    def setHTMLport(self, x):
        with open("upload.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        
        if (self.f == False):
            html_content = html_content.replace("{url}", x)
            self.f = True
        else:
            html_content = html_content.replace("{}".format(self.ip + ':' + str(self.port)), x)
            self.f = False

        with open("upload.html", "w", encoding="utf-8") as file:
            file.write(html_content)       