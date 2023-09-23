# https://pythonhosted.org/PyQRCode/
import pyqrcode
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QImage
from PyQt6.QtSvg import QSvgRenderer
from io import BytesIO


class QRcode (QSvgRenderer):
    def __init__(self):
        super().__init__()
        url = pyqrcode.create('Knights who say ni!')
        # in-memory stream
        buffer = BytesIO()
        url.svg(buffer)
        url.svg('uca.svg', scale=4, background="#15648C", module_color="#7D007D")
        # do whatever you want with buffer.getvalue()
        # print(list(buffer.getvalue()))
        # Print the QR
        # url.show()
        # Close the buffer
        buffer.close()
