from PyQt6.QtGui import QPixmap


class CustomQImage(QPixmap):
    def __init__(self, image=0):
        folder = '/Users/jaimegonzalezquirarte/PycharmProjects/Ixchel/assets/icons/statuses/'
        self.possible_images = [folder + "medicated.png",
                                folder + "aids.png",
                                folder + "cancer.png",
                                folder + "diabetes.png",
                                folder + "dna.png",
                                folder + "heart.png"]
        super().__init__(self.possible_images[image])
