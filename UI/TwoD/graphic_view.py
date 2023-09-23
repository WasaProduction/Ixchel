from UI.Widgets.image_button import ImageButton
from PyQt6.QtWidgets import QGraphicsView
from PyQt6.QtGui import QBrush, QColor
from UI.TwoD.skeleton_graphic_scene import SkeletonGraphicScene


class GraphicView(QGraphicsView):
    def __init__(self, parent=None, scene=None):
        super(GraphicView, self).__init__(parent)
        self.scene = SkeletonGraphicScene()
        self.init_ui()

    def update_button(self):
        self.scene.update_button()


    """     UI      """
    def init_ui(self):
        self.setScene(self.scene)
        self.setBackgroundBrush(QColor(49, 154, 94))
