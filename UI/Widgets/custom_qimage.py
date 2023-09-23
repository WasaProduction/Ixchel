from PyQt6.QtGui import QPixmap


class CustomQImage(QPixmap):
    def __init__(self, image=0):
        self.possible_images = ["/Users/jaimegonzalezquirarte/Desktop/App/Statuses_Icons/Zodiaco_Aquarius.png",
                                "/Users/jaimegonzalezquirarte/Desktop/App/Statuses_Icons/Zodiaco_Aries.png",
                                "/Users/jaimegonzalezquirarte/Desktop/App/Statuses_Icons/lego.png"]
        super().__init__(self.possible_images[image])
