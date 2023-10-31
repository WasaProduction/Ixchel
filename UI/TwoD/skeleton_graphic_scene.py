from PyQt6.QtWidgets import QGraphicsScene, QGraphicsProxyWidget
from PyQt6.QtGui import QColor
from data_models.anatomy.skeleton.full_skeleton import FullSkeleton


class SkeletonGraphicScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(SkeletonGraphicScene, self).__init__(parent)
        #   Button details
        button_size = ButtonSize()
        self.buttons = []
        self.proxys = []
        self.b_w = button_size.width
        self.b_h = button_size.height
        #   This object contains all the bones separated by sections
        self.full_skeleton = FullSkeleton()
        #   Call placing functions
        self.place_bones()

    def place_bones(self):
        """     Placing bones       """
        #   To avoid a huge function by placing all the bones here the process has been separated by sections
        self.place_head_bones()
        self.place_neck_bones()

    def update_skeleton(self):
        self.full_skeleton.update_skeleton()

    def color_select(self):
        color = QColor(255, 192, 203)
        return color

    def opacity_select(self):
        return 0.5

    def place_head_bones(self):
        """     Cranium     """
        #   Frontal
        bone = self.full_skeleton.cranium.frontal
        self.place_proxy(bone, self.b_w * 4, 0)
        #   Parietal
        bone = self.full_skeleton.cranium.right_parietal
        self.place_proxy(bone, self.b_w * 5, 0)
        bone = self.full_skeleton.cranium.left_parietal
        self.place_proxy(bone, self.b_w * 3, 0)
        #   Temporal
        bone = self.full_skeleton.cranium.right_temporal
        self.place_proxy(bone, self.b_w * 3, self.b_h * 3)
        bone = self.full_skeleton.cranium.right_temporal
        self.place_proxy(bone, self.b_w * 5, self.b_h * 3)
        #   Occipital
        bone = self.full_skeleton.cranium.occipital
        self.place_proxy(bone, self.b_w * 4, self.b_h * 3)
        #   Sphenoid
        bone = self.full_skeleton.cranium.sphenoid
        self.place_proxy(bone, self.b_w * 4, self.b_h)
        #   Ethmoid
        bone = self.full_skeleton.cranium.ethmoid
        self.place_proxy(bone, self.b_w * 4, self.b_h * 2)
        """     Ear         """
        """
        #   Right
        bone = ImageButton(pixmap=full_skeleton.right_ear.malleus.image, text=full_skeleton.right_ear.malleus.name)
        #self.place_proxy(bone, self.b_w * 5, self.b_h)
        bone = ImageButton(pixmap=full_skeleton.right_ear.incus.image, text=full_skeleton.right_ear.incus.name)
        #self.place_proxy(bone, self.b_w * 6, self.b_h)
        bone = ImageButton(pixmap=full_skeleton.right_ear.stapes.image, text=full_skeleton.right_ear.stapes.name)
        #self.place_proxy(bone, self.b_w * 7, self.b_h)
        #   Left
        bone = ImageButton(pixmap=full_skeleton.right_ear.malleus.image, text=full_skeleton.left_ear.malleus.name)
        #self.place_proxy(bone, self.b_w, self.b_h)
        bone = ImageButton(pixmap=full_skeleton.right_ear.incus.image, text=full_skeleton.left_ear.incus.name)
        #self.place_proxy(bone, self.b_w * 2, self.b_h)
        bone = ImageButton(pixmap=full_skeleton.right_ear.stapes.image, text=full_skeleton.left_ear.stapes.name)
        #self.place_proxy(bone, self.b_w * 3, self.b_h)
        """
        """     Facial      """
        #   Zygomatic
        """
        bone = ImageButton(pixmap=full_skeleton.facial.right_zygomatic.image, text=full_skeleton.facial.right_zygomatic.name)
        #self.place_proxy(bone, self.b_w * 5, self.b_h * 2)
        bone = ImageButton(pixmap=full_skeleton.facial.left_zygomatic.image, text=full_skeleton.facial.left_zygomatic.name)
        #self.place_proxy(bone, self.b_w * 3, self.b_h * 2)
        #   Maxilla
        bone = ImageButton(pixmap=full_skeleton.facial.right_maxilla.image, text=full_skeleton.facial.right_maxilla.name)
        #self.place_proxy(bone, self.b_w * 6, self.b_h * 5)
        bone = ImageButton(pixmap=full_skeleton.facial.left_maxilla.image, text=full_skeleton.facial.left_maxilla.name)
        #self.place_proxy(bone, self.b_w * 2, self.b_h * 5)
        #   Nasal
        bone = ImageButton(pixmap=full_skeleton.facial.right_nasal.image, text=full_skeleton.facial.right_nasal.name)
        #self.place_proxy(bone, self.b_w * 5, self.b_h * 4)
        bone = ImageButton(pixmap=full_skeleton.facial.left_nasal.image, text=full_skeleton.facial.left_nasal.name)
        #self.place_proxy(bone, self.b_w * 3, self.b_h * 4)
        #   Vomer
        bone = ImageButton(pixmap=full_skeleton.facial.vomer.image, text=full_skeleton.facial.vomer.name)
        #self.place_proxy(bone, self.b_w * 4, self.b_h * 4)
        #   Lacrimal
        bone = ImageButton(pixmap=full_skeleton.facial.right_lacrimal.image, text=full_skeleton.facial.right_lacrimal.name)
        #self.place_proxy(bone, self.b_w * 6, self.b_h * 4)
        bone = ImageButton(pixmap=full_skeleton.facial.left_lacrimal.image, text=full_skeleton.facial.left_lacrimal.name)
        #self.place_proxy(bone, self.b_w * 2, self.b_h * 4)
        #   Palatine
        bone = ImageButton(pixmap=full_skeleton.facial.right_palatine.image, text=full_skeleton.facial.right_palatine.name)
        #self.place_proxy(bone, self.b_w * 5, self.b_h * 6)
        bone = ImageButton(pixmap=full_skeleton.facial.left_palatine.image, text=full_skeleton.facial.left_palatine.name)
        #self.place_proxy(bone, self.b_w * 3, self.b_h * 6)
        #   Nasal conchae
        bone = ImageButton(pixmap=full_skeleton.facial.right_inferior_nasal_conchae.image, text=full_skeleton.facial.right_inferior_nasal_conchae.name)
        #self.place_proxy(bone, self.b_w * 5, self.b_h * 5)
        bone = ImageButton(pixmap=full_skeleton.facial.left_inferior_nasal_conchae.image, text=full_skeleton.facial.left_inferior_nasal_conchae.name)
        #self.place_proxy(bone, self.b_w * 3, self.b_h * 5)
        #   Mandible
        bone = ImageButton(pixmap=full_skeleton.facial.mandible.image, text=full_skeleton.facial.mandible.name)
        #self.place_proxy(bone, self.b_w * 4, self.b_h * 7)
        """
    def place_neck_bones(self):
        """     Neck     """
        #   Hyoid
        #bone = ImageButton(pixmap=full_skeleton.hyoid.image, text=full_skeleton.hyoid.name)
        #self.place_proxy(bone, self.b_w * 4, self.b_h * 8)

    def place_thorax_bones(self, full_skeleton):
        """     Thorax     """
        """
        #   Sternum
        bone = ImageButton(full_skeleton.hyoid.image)
        self.place_proxy(bone, self.b_w, self.b_h)
        """
        """     Ribs        """
        """
        #   Accessory
        bone = ImageButton(full_skeleton.r_a01.image)
        bone = ImageButton(full_skeleton.l_a01.image)
        #   Rib-sternum (T01 - T07)
        bone = ImageButton(full_skeleton.r_t01.image)
        bone = ImageButton(full_skeleton.l_t01.image)
        bone = ImageButton(full_skeleton.r_t07.image)
        bone = ImageButton(full_skeleton.l_t07.image)
        #   Rib-rib-sternum (T08 - T10)
        bone = ImageButton(full_skeleton.r_t08.image)
        bone = ImageButton(full_skeleton.l_t08.image)
        bone = ImageButton(full_skeleton.r_t09.image)
        bone = ImageButton(full_skeleton.l_t09.image)
        bone = ImageButton(full_skeleton.r_t10.image)
        bone = ImageButton(full_skeleton.l_t10.image)
        #   Rib-floating (T11 - T12)
        bone = ImageButton(full_skeleton.r_t11.image)
        bone = ImageButton(full_skeleton.l_t11.image)
        bone = ImageButton(full_skeleton.r_t12.image)
        bone = ImageButton(full_skeleton.l_t12.image)
        """
    def place_vertebrae_bones(self, full_skeleton):
        """     Vertebrae     """
        pass

    def place_shoulder_bones(self, full_skeleton):
        """     Shoulder     """
        pass

    def place_arms_bones(self, full_skeleton):
        """     Arms     """
        pass

    def place_pelvis_bones(self, full_skeleton):
        """     Pelvis     """
        pass

    def place_legs_bones(self, full_skeleton):
        """     Legs     """
        pass

    def place_proxy(self, bone, x, y, ):
        self.buttons.append(bone.button)
        proxy = QGraphicsProxyWidget()
        proxy.setWidget(bone.button)
        self.proxys.append(proxy)
        #   Set the position of the button within the scene
        proxy.setPos(x, y)
        #   Place the widget
        self.addItem(proxy)


class ButtonSize:
    def __init__(self):
        self.height = 30
        self.width = 30
