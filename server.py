from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
from filetransfer import FileUploadHandler

class Server:
    def __init__(self, ip=None, port = 8000):
        self.ip = ip
        self.port = port       

    def run(self):
        server_class = HTTPServer
        handler_class = FileUploadHandler
        server_address = (self.ip if self.ip else '', self.port)  # If ip is specified, uses it, if not, it listens to all ips on that specific port
        httpd = server_class(server_address, handler_class)
        httpd.serve_forever()
        
    def makedir(self, name):
        os.makedirs(name, exist_ok=True)
        print('Path {} created succesfully!'.format(name))