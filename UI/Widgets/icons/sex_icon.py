from PyQt6.QtWidgets import QPushButton, QSizePolicy
from PyQt6.QtGui import QIcon


class SexIconWidget(QPushButton):
    def __init__(self, parent=None, birth_sex='None', current_sex='None'):
        super(SexIconWidget, self).__init__(parent)
        self.folder = '/Users/jaimegonzalezquirarte/PycharmProjects/Ixchel/assets/icons/sex/'
        #   Used to determine icon.
        self.birth_sex = birth_sex
        self.current_sex = current_sex
        #   Initialize.
        self.setIcon(QIcon(self.folder + "male.png"))
        #   Select image:
        self.update_icon()
        #   Customize.
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        #   Remove border
        self.setStyleSheet("border: none;")

    def update_icon(self, birth_sex=0, current_sex='None'):
        #   Update parameters.
        self.birth_sex = birth_sex
        self.current_sex = current_sex
        #   Run selection
        self.choose_icon()

    def choose_icon(self):
        if self.birth_sex == 'female' and self.current_sex == 'female':
            self.setIcon(QIcon(self.folder + 'female.png'))
            self.setToolTip('Woman')
        elif self.birth_sex == 'male' and self.current_sex == 'male':
            self.setIcon(QIcon(self.folder + 'male.png'))
            self.setToolTip('Man')
        elif self.birth_sex == 'female' and self.current_sex == 'male':
            self.setIcon(QIcon(self.folder + "trans_male.png"))
            self.setToolTip('Trans-male')
        elif self.birth_sex == 'male' and self.current_sex == 'female':
            self.setIcon(QIcon(self.folder + "trans_female.png"))
            self.setToolTip("Trans-female")
        else:
            #   Unexpected scenario.
            self.setIcon(QIcon(self.folder + "trans_male.png"))
            self.setToolTip("Nope")
