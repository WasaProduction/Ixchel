from PyQt6.QtGui import QPixmap
"""
For bone
Classes:
    Bone
"""


class Bone:
    def __init__(self, bone_id=0, image_path=None, name=None):
        if image_path is not None:
            #   TODO set bone missing image
            default_path = '/Users/jaimegonzalezquirarte/Desktop/App/Statuses_Icons/Zodiaco_Aquarius.png'
            self.image = QPixmap(default_path)
        self.image = QPixmap(image_path)
        self.name = name
        self.bone_id = bone_id
