import time
from PyQt6.QtWidgets import QToolButton, QWidget, QSizePolicy, QFrame, QScrollArea, QVBoxLayout, QLabel
from PyQt6.QtCore import QAbstractAnimation, QParallelAnimationGroup, QPropertyAnimation, Qt, pyqtSlot, QTimer, \
    pyqtSignal


class CollapsibleBox(QWidget):
    #   Custom signal.
    toggled_signal = pyqtSignal(int)

    def __init__(self, parent=None, title=None, content=None):
        super(CollapsibleBox, self).__init__(parent)
        if title is None:
            self.title = 'Missing title'
        else:
            self.title = title
        if content is None:
            self.received_content = QLabel('Nothing to display')
        else:
            self.received_content = content
        #   Toggle button
        self.toggle_button = self.create_toggle_button(self.title)
        #   Flag to prevent button spamming
        self.button_enabled = True
        #   Timer to re-enable the button after a delay
        self.re_enable_timer = QTimer()
        self.re_enable_timer.timeout.connect(self.enable_button)
        #   Expanded flag
        self.expanded = True
        # Use proxy to place received_content
        self.proxy_content_widget = QWidget()
        self.proxy_content_widget.setStyleSheet('background red')
        self.proxy_v_lay = QVBoxLayout(self.proxy_content_widget)
        self.received_content_into_proxy()
        """     Layout      """
        self.my_layout = self.create_layout()
        #   Add widgets
        self.my_layout.addWidget(self.toggle_button)
        self.my_layout.addWidget(self.proxy_content_widget)
        self.setLayout(self.my_layout)
        """     Animations      """
        #   Animations to be executed simultaneously
        self.toggle_animation = self.create_anim_group()
        #   Calculate heights
        self.collapsed_height = self.calculate_collapsed_height()
        self.content_height = self.calculate_content_height()
        #   Tune animations based on heights
        self.tune_anim_group()
        #   Expandable.
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    @staticmethod
    def calculate_collapsed_height():
        return 25

    def calculate_content_height(self):
        return self.proxy_content_widget.sizeHint().height() + self.calculate_collapsed_height()

    def tune_anim_group(self):
        for i in range(self.toggle_animation.animationCount()):
            #   Settings for animations inside the group (for the widget containing the scroll area)
            animation = self.toggle_animation.animationAt(i)
            #   Animation in ms, 500 makes it smooth
            animation.setDuration(500)
            #   Height will change from collapsed
            animation.setStartValue(self.collapsed_height)
            #   To collapsed plus the contents.
            animation.setEndValue(self.collapsed_height + self.content_height)

    def create_anim_group(self):
        toggle_animation = QParallelAnimationGroup(self)
        toggle_animation.addAnimation(QPropertyAnimation(self, b"minimumHeight"))
        toggle_animation.addAnimation(QPropertyAnimation(self, b"maximumHeight"))
        toggle_animation.addAnimation(QPropertyAnimation(self.proxy_content_widget, b"maximumHeight"))
        # toggle_animation.addAnimation(QPropertyAnimation(self.content_area, b"maximumHeight"))
        return toggle_animation

    def create_layout(self):
        #   Configure layout
        my_layout = QVBoxLayout(self)
        my_layout.setSpacing(0)
        my_layout.setContentsMargins(0, 0, 0, 0)
        return my_layout

    def remove_proxy_content(self):
        self.proxy_v_lay.removeWidget(self.received_content)
        pass

    def received_content_into_proxy(self):
        self.proxy_v_lay.addWidget(self.received_content)

    def force_collapse(self):
        if self.expanded:
            self.button_enabled = True
            self.on_clicked()

    def update_content(self, content=None):
        #   TODO Fix update content of collapsible box while expanded
        #   Prevent bug
        self.force_collapse()
        time.sleep(5.5)
        self.actually_update_content(content)

    def actually_update_content(self, content=None):
        self.received_content = content
        self.received_content_into_proxy()
        #   Calculate heights
        self.collapsed_height = self.calculate_collapsed_height()
        self.content_height = self.calculate_content_height()
        #   Tune animations based on heights
        self.tune_anim_group()

    def update_height(self, height=0):
        #   Calculate heights
        self.collapsed_height = self.calculate_collapsed_height()
        self.content_height = height if height != 0 else self.calculate_content_height()
        #self.proxy_content_widget.setMinimumHeight(height if height != 0 else self.calculate_content_height())
        self.tune_anim_group()

    def create_toggle_button(self, title):
        toggle_button = QToolButton()
        # Set stylesheet to remove the border
        toggle_button.setStyleSheet("border: none;")
        toggle_button.setText(title)
        toggle_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        toggle_button.setArrowType(Qt.ArrowType.RightArrow)
        toggle_button.clicked.connect(self.on_clicked)
        return toggle_button

    #   TODO remove function
    @staticmethod
    def create_content_area():
        content_area = QScrollArea()
        content_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        content_area.setMinimumHeight(0)
        content_area.setMaximumHeight(1)
        content_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        content_area.setFrameShape(QFrame.Shape.NoFrame)
        return content_area

    def play_animation(self):
        # Change the arrow on the button
        self.toggle_button.setArrowType(Qt.ArrowType.DownArrow if not self.expanded else Qt.ArrowType.RightArrow)
        # Set the animation direction
        self.toggle_animation.setDirection(QAbstractAnimation.Direction.Forward if not self.expanded else
                                           QAbstractAnimation.Direction.Backward)
        # Call the animation group
        self.toggle_animation.start()

    @pyqtSlot()
    def on_clicked(self):
        if self.button_enabled:
            #   Replace arrow & expand/collapse.
            self.play_animation()
            # Revert the button status.
            self.toggle_button.setChecked(not self.toggle_button.isChecked())
            #   Reset expanded flag.
            self.expanded = not self.expanded
            #   Emit height via signal.
            self.toggled_signal.emit(self.content_height if self.expanded else self.collapsed_height)
            self.button_enabled = False
            #   Re-enable the button after x time.
            self.re_enable_timer.start(1000)

    def enable_button(self):
        #   Prevent button spamming
        self.button_enabled = True
        self.re_enable_timer.stop()
