from PyQt6.QtGui import QPixmap
from UI.TwoD.bone_button import BoneButton
"""
For bone
Classes:
    Bone
"""


class Bone:
    def __init__(self, bone_id=0, image_path=None, name=None, width=50, height=50, status=0, colors=None):
        if image_path is not None:
            #   TODO set bone missing image
            default_path = '/Users/jaimegonzalezquirarte/Desktop/App/Statuses_Icons/Zodiaco_Aquarius.png'
            self.image = QPixmap(default_path)
        self.image = QPixmap(image_path)
        self.name = name
        self.bone_id = bone_id
        #   Button W, H
        self.width = width
        self.height = height
        self.status = status
        self.colors = colors
        self.button = BoneButton(pixmap=self.image, text=self.name, width=self.width, height=self.height)

    def update_bone(self, status=0, opacity=None):
        self.status = status
        #   Update button.
        if self.status == 0:
            #   Remove tint
            self.button.update_button()
        else:
            #   Apply tint
            self.button.update_button(color=self.colors[self.status])
        pass
