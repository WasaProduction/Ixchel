from PyQt6.QtWidgets import QGraphicsOpacityEffect, QPushButton
from mongodb.read.translate_tags_to_names import TranslateTagsNames
from mongodb.read.get_color import GetColor


# Receive string for the label, type for the color, severity for opacity
class TagIndividualWidget(QPushButton):
    def __init__(self, tag):
        super().__init__()
        self.setText(tag.name)
        # setting geometry of button
        self.setStyleSheet(f"border-width: 4px 4px 4px 4px; "
                           f"border-radius: 10px; "
                           f"border-style: solid; "
                           f"border-color: #{tag.color};")
        self.setToolTip(tag.creation_date.strftime("%d/%m/%Y"))
        # Each severity level will increase opacity by .5
        self.opacity = 1 * .5
        tag_opacity = QGraphicsOpacityEffect()
        # Setting opacity by default .5
        tag_opacity.setOpacity(.5 + self.opacity)
        self.setGraphicsEffect(tag_opacity)
