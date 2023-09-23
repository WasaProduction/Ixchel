from UI.Widgets.image_button import ImageButton
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsProxyWidget
from PyQt6.QtGui import QColor
from data_models.anatomy.skeleton.full_skeleton import FullSkeleton


class SkeletonGraphicScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(SkeletonGraphicScene, self).__init__(parent)
        #   Button details
        button_size = ButtonSize()
        self.buttons = {}
        self.proxys = {}
        self.b_w = button_size.width
        self.b_h = button_size.height
        #   Call placing functions
        self.place_bones()

    def place_bones(self):
        #   This object contains all the bones separated by sections
        full_skeleton = FullSkeleton()
        """     Placing bones       """
        #   To avoid a huge function by placing all the bones here the process has been separated by sections
        self.place_head_bones(full_skeleton)
        self.place_neck_bones(full_skeleton)

    def update_button(self):
        print(self.items())
        for item in self.items():
            print(item.widget())
        #self.proxys.
        #self.bone.update_button_tint(self.bone, self.color_select(), 1)

    def color_select(self):
        color = QColor(255, 192, 203)
        return color

    def opacity_select(self):
        return 0.5

    def place_head_bones(self, full_skeleton):
        """     Cranium     """
        #   Frontal
        self.bone = ImageButton(pixmap=full_skeleton.cranium.frontal.image, text=full_skeleton.cranium.frontal.name)
        self.place_proxy(self.bone, self.b_w * 4, 0)
        #   Parietal
        bone = ImageButton(pixmap=full_skeleton.cranium.right_parietal.image, text=full_skeleton.cranium.right_parietal.name)
        self.place_proxy(bone, self.b_w * 5, 0)
        bone = ImageButton(pixmap=full_skeleton.cranium.left_parietal.image, text=full_skeleton.cranium.left_parietal.name)
        self.place_proxy(bone, self.b_w * 3, 0)
        #   Temporal
        bone = ImageButton(pixmap=full_skeleton.cranium.right_temporal.image, text=full_skeleton.cranium.left_temporal.name)
        self.place_proxy(bone, self.b_w * 3, self.b_h * 3)
        bone = ImageButton(pixmap=full_skeleton.cranium.right_temporal.image, text=full_skeleton.cranium.right_temporal.name)
        self.place_proxy(bone, self.b_w * 5, self.b_h * 3)
        #   Occipital
        bone = ImageButton(pixmap=full_skeleton.cranium.occipital.image, text=full_skeleton.cranium.occipital.name)
        self.place_proxy(bone, self.b_w * 4, self.b_h * 3)
        #   Sphenoid
        bone = ImageButton(pixmap=full_skeleton.cranium.sphenoid.image, text=full_skeleton.cranium.sphenoid.name)
        self.place_proxy(bone, self.b_w * 4, self.b_h)
        #   Ethmoid
        bone = ImageButton(pixmap=full_skeleton.cranium.ethmoid.image, text=full_skeleton.cranium.ethmoid.name)
        self.place_proxy(bone, self.b_w * 4, self.b_h * 2)
        """     Ear         """
        #   Right
        bone = ImageButton(pixmap=full_skeleton.right_ear.malleus.image, text=full_skeleton.right_ear.malleus.name)
        self.place_proxy(bone, self.b_w * 5, self.b_h)
        bone = ImageButton(pixmap=full_skeleton.right_ear.incus.image, text=full_skeleton.right_ear.incus.name)
        self.place_proxy(bone, self.b_w * 6, self.b_h)
        bone = ImageButton(pixmap=full_skeleton.right_ear.stapes.image, text=full_skeleton.right_ear.stapes.name)
        self.place_proxy(bone, self.b_w * 7, self.b_h)
        #   Left
        bone = ImageButton(pixmap=full_skeleton.right_ear.malleus.image, text=full_skeleton.left_ear.malleus.name)
        self.place_proxy(bone, self.b_w, self.b_h)
        bone = ImageButton(pixmap=full_skeleton.right_ear.incus.image, text=full_skeleton.left_ear.incus.name)
        self.place_proxy(bone, self.b_w * 2, self.b_h)
        bone = ImageButton(pixmap=full_skeleton.right_ear.stapes.image, text=full_skeleton.left_ear.stapes.name)
        self.place_proxy(bone, self.b_w * 3, self.b_h)
        """     Facial      """
        #   Zygomatic
        bone = ImageButton(pixmap=full_skeleton.facial.right_zygomatic.image, text=full_skeleton.facial.right_zygomatic.name)
        self.place_proxy(bone, self.b_w * 5, self.b_h * 2)
        bone = ImageButton(pixmap=full_skeleton.facial.left_zygomatic.image, text=full_skeleton.facial.left_zygomatic.name)
        self.place_proxy(bone, self.b_w * 3, self.b_h * 2)
        #   Maxilla
        bone = ImageButton(pixmap=full_skeleton.facial.right_maxilla.image, text=full_skeleton.facial.right_maxilla.name)
        self.place_proxy(bone, self.b_w * 6, self.b_h * 5)
        bone = ImageButton(pixmap=full_skeleton.facial.left_maxilla.image, text=full_skeleton.facial.left_maxilla.name)
        self.place_proxy(bone, self.b_w * 2, self.b_h * 5)
        #   Nasal
        bone = ImageButton(pixmap=full_skeleton.facial.right_nasal.image, text=full_skeleton.facial.right_nasal.name)
        self.place_proxy(bone, self.b_w * 5, self.b_h * 4)
        bone = ImageButton(pixmap=full_skeleton.facial.left_nasal.image, text=full_skeleton.facial.left_nasal.name)
        self.place_proxy(bone, self.b_w * 3, self.b_h * 4)
        #   Vomer
        bone = ImageButton(pixmap=full_skeleton.facial.vomer.image, text=full_skeleton.facial.vomer.name)
        self.place_proxy(bone, self.b_w * 4, self.b_h * 4)
        #   Lacrimal
        bone = ImageButton(pixmap=full_skeleton.facial.right_lacrimal.image, text=full_skeleton.facial.right_lacrimal.name)
        self.place_proxy(bone, self.b_w * 6, self.b_h * 4)
        bone = ImageButton(pixmap=full_skeleton.facial.left_lacrimal.image, text=full_skeleton.facial.left_lacrimal.name)
        self.place_proxy(bone, self.b_w * 2, self.b_h * 4)
        #   Palatine
        bone = ImageButton(pixmap=full_skeleton.facial.right_palatine.image, text=full_skeleton.facial.right_palatine.name)
        self.place_proxy(bone, self.b_w * 5, self.b_h * 6)
        bone = ImageButton(pixmap=full_skeleton.facial.left_palatine.image, text=full_skeleton.facial.left_palatine.name)
        self.place_proxy(bone, self.b_w * 3, self.b_h * 6)
        #   Nasal conchae
        bone = ImageButton(pixmap=full_skeleton.facial.right_inferior_nasal_conchae.image, text=full_skeleton.facial.right_inferior_nasal_conchae.name)
        self.place_proxy(bone, self.b_w * 5, self.b_h * 5)
        bone = ImageButton(pixmap=full_skeleton.facial.left_inferior_nasal_conchae.image, text=full_skeleton.facial.left_inferior_nasal_conchae.name)
        self.place_proxy(bone, self.b_w * 3, self.b_h * 5)
        #   Mandible
        bone = ImageButton(pixmap=full_skeleton.facial.mandible.image, text=full_skeleton.facial.mandible.name)
        self.place_proxy(bone, self.b_w * 4, self.b_h * 7)

    def place_neck_bones(self, full_skeleton):
        """     Neck     """
        #   Hyoid
        bone = ImageButton(pixmap=full_skeleton.hyoid.image, text=full_skeleton.hyoid.name)
        self.place_proxy(bone, self.b_w * 4, self.b_h * 8)

    def place_thorax_bones(self, full_skeleton):
        """     Thorax     """
        #   Sternum
        bone = ImageButton(full_skeleton.hyoid.image)
        self.place_proxy(bone, self.b_w, self.b_h)
        """     Ribs        """
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

    def place_proxy(self, button, x, y, ):
        self.buttons[button.text] = button
        self.proxys['cranium_frontal'] = self.bone
        proxy = QGraphicsProxyWidget()
        proxy.setWidget(button)
        #   Set the position of the button within the scene
        proxy.setPos(x, y)
        #   Place the widget
        self.addItem(proxy)


class ButtonSize:
    def __init__(self):
        self.height = 30
        self.width = 30
