from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtCore import QTimer


class CustomSearchBar(QLineEdit):
    def __init__(self, parent=None, placeholder=None, function=None):
        super().__init__(parent)
        self.setPlaceholderText(placeholder)
        self.my_function = function
        #   Connect return to function.
        self.returnPressed.connect(lambda: self.execute_function())
        """     Shaking     """
        self.shake_timer = QTimer(self)
        self.shake_timer.timeout.connect(self.update_position)
        #   ms
        self.shake_duration = 100
        self.max_shakes = 4
        self.shakes_remaining = 0

    def execute_function(self):
        if self.my_function is not None:
            self.my_function()

    def shake(self):
        if self.shakes_remaining == 0:
            self.original_position = self.pos()
            self.shakes_remaining = self.max_shakes
        self.shake_timer.start(self.shake_duration)

    def update_position(self):
        if self.shakes_remaining > 0:
            self.shakes_remaining -= 1
            dx = 5 if self.shakes_remaining % 2 == 0 else -5
            self.move(self.original_position.x() + dx, self.original_position.y())
        else:
            self.move(self.original_position)
            self.shake_timer.stop()
