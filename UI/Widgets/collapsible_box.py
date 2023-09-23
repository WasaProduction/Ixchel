from PyQt6.QtWidgets import QToolButton, QWidget, QSizePolicy, QFrame, QScrollArea, QVBoxLayout
from PyQt6.QtCore import QAbstractAnimation, QParallelAnimationGroup, QPropertyAnimation, Qt, pyqtSlot


class CollapsibleBox(QWidget):
    def __init__(self, parent=None, title="Title", content=None):
        super(CollapsibleBox, self).__init__(parent)
        self.tag_list = []
        # Toggle button
        self.toggle_button = QToolButton()
        self.toggle_button.setCheckable(True)
        self.toggle_button.setChecked(False)
        self.toggle_button.setText(title)
        self.toggle_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(Qt.ArrowType.RightArrow)
        self.toggle_button.pressed.connect(self.on_pressed)
        self.toggle_animation = QParallelAnimationGroup(self)

        # Expandable area
        self.content_area = QScrollArea(maximumHeight=0, minimumHeight=0)
        self.content_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.content_area.setFrameShape(QFrame.Shape.NoFrame)

        my_layout = QVBoxLayout(self)
        my_layout.setSpacing(0)
        my_layout.setContentsMargins(0, 0, 0, 0)

        # Content inside expandable area
        content_widget = QWidget()
        v_lay = QVBoxLayout()
        v_lay.addWidget(content)
        content_widget.setLayout(v_lay)
        self.content_area.setWidget(content_widget)

        my_layout.addWidget(self.toggle_button)
        my_layout.addWidget(self.content_area)

        self.toggle_animation.addAnimation(QPropertyAnimation(self, b"minimumHeight"))
        self.toggle_animation.addAnimation(QPropertyAnimation(self, b"maximumHeight"))
        self.toggle_animation.addAnimation(QPropertyAnimation(self.content_area, b"maximumHeight"))

        collapsed_height = (self.sizeHint().height() - self.content_area.maximumHeight())
        content_height = content_widget.sizeHint().height()

        for i in range(self.toggle_animation.animationCount()):
            # Settings for animations inside the group (for the widget containing the scroll area)
            animation = self.toggle_animation.animationAt(i)
            # Animation in ms, 500 makes it smooth
            animation.setDuration(500)
            # Height will change from collapsed
            animation.setStartValue(collapsed_height)
            # to collapsed plus the contents.
            animation.setEndValue(collapsed_height + content_height)
        # Override animation for the last animation (affects only the scroll area)
        content_animation = self.toggle_animation.animationAt(self.toggle_animation.animationCount() - 1)
        content_animation.setDuration(500)
        content_animation.setStartValue(0)
        content_animation.setEndValue(content_height)

    @pyqtSlot()
    def on_pressed(self):
        # Get the check status of the button
        checked = self.toggle_button.isChecked()
        # Change the arrow on the button
        self.toggle_button.setArrowType(Qt.ArrowType.DownArrow if not checked else Qt.ArrowType.RightArrow)
        # Set the animation direction
        self.toggle_animation.setDirection(QAbstractAnimation.Direction.Forward if not checked else
                                           QAbstractAnimation.Direction.Backward)
        # Call the animation group
        self.toggle_animation.start()
        # Revert the button status
        self.toggle_button.setChecked(not self.toggle_button.isChecked())
