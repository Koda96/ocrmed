import cv2
import pytesseract
from server import Server, FileUploadHandler

if __name__ == "__main__":
    try:
        try:
            #port = int(input("Type server port to listen to\n"))
            server = Server(port = 8000)
        except TypeError:
            print("A port number is needed to run the server, please make sure to use only integers")
        except EOFError:
            print("Port number can't be blank")
        else:
            print("Server succesfully started on port {}".format(server.port))
            server.makedir("uploads")
            server.run()
    except KeyboardInterrupt:
            print("Server stopped succesfully from KeyboardInterrupt")
    finally:
            print("Server stopped listening to port {}".format(server.port))