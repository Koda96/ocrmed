from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import cgi

class FileUploadHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        #If a file is received using the POST integrated method from http.server, the content-type is extracted using the parse_header function
        #from the cgi library, then it is formatted to bytes to correctly parse the data with the parse_multipart function from cgi
        #this is to make sure the parser is receiving a byte type variable and not a string, which may cause problems in the integrity of the data
        ctype, pdict = cgi.parse_header(self.headers.get('Content-Type'))
        if ctype == 'multipart/form-data':
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            fields = cgi.parse_multipart(self.rfile, pdict)
            file_data = fields.get('file')[0]
            file_name = fields.get('filename')[0]
        
            #Uploading the file to 'uploads' folder using wb (write, binary) type
            with open(os.path.join('uploads', file_name), 'wb') as f:
                f.write(file_data)
            
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'File uploaded succesfully')
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Invalid request') 