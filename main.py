import cv2
import pytesseract
from server import Server
from filetransfer import FileUploadHandler

if __name__ == "__main__":
    serv = Server()
    serv.start()