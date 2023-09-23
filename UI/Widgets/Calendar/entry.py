import json
from PyQt6.QtWidgets import QFrame, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from data_models.agenda_entry import AgendaEntry
from UI.Widgets.image_button import ImageButton


class FrameEntry(QFrame):
    def __init__(self, parent=None, entry=None):
        super().__init__(parent)
        self.my_layout = QVBoxLayout()
        #   Customize UI
        self.init_ui()
        #   Add widget
        self.my_layout.addWidget(Entry(self, entry))
        #   Apply layout
        self.setLayout(self.my_layout)

    """     UI      """
    def init_ui(self):
        self.setFrameStyle(QFrame.Shape.StyledPanel)
        self.setFrameShadow(QFrame.Shadow.Sunken)
        self.my_layout.setContentsMargins(0, 0, 0, 0)


class Entry(QWidget):
    def __init__(self, parent=None, entry=None):
        super().__init__(parent)
        #   Prevent None
        if entry is None:
            self.my_entry = AgendaEntry()
        else:
            self.my_entry = entry
        #   Entry sentence.
        my_sentence = '{}'.format(self.my_entry['id_attendee'])
        #   Omit seconds.
        my_time = '{}-{}'.format(self.my_entry['start'].time().strftime("%X")[:-3],
                                 self.my_entry['end'].time().strftime("%X")[:-3])

        """     Widget/layout containing name & time        """
        n_t_lyt = QVBoxLayout()
        #   Remove margins
        n_t_lyt.setContentsMargins(0, 0, 0, 0)
        #   Remove spacing
        n_t_lyt.setSpacing(0)
        #   Create labels
        entry_name = QLabel(my_sentence)
        entry_time = QLabel(my_time)
        #   Align labels center
        entry_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        entry_time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #   Add labels to layout
        n_t_lyt.addWidget(entry_name)
        n_t_lyt.addWidget(entry_time)
        #   Container widget
        txt_wgt = QWidget()
        #   Apply layout to container
        txt_wgt.setLayout(n_t_lyt)
        """     Widget/layout containing edit & delete buttons      """
        e_d_lyt = QVBoxLayout()
        #   Remove margins
        e_d_lyt.setContentsMargins(0, 0, 0, 0)
        #   Remove spacing
        e_d_lyt.setSpacing(0)
        #   Create buttons
        delete_btn = QPushButton('Delete')
        edit_btn = QPushButton('Edit')
        #   Connect buttons
        delete_btn.clicked.connect(lambda: self.delete_entry())
        edit_btn.clicked.connect(lambda: self.edit_entry())
        #   Add buttons to layout
        e_d_lyt.addWidget(delete_btn)
        e_d_lyt.addWidget(edit_btn)
        #   Container widget
        self.buttons_wgt = QWidget()
        #   Apply layout to container
        self.buttons_wgt.setLayout(e_d_lyt)
        #   Hide widget by default
        self.buttons_wgt.hide()
        """     Widget/layout containing labels & delete button     """
        h_lyt = QHBoxLayout()
        #   Remove margins
        h_lyt.setContentsMargins(0, 0, 0, 0)
        #   Adding container widgets
        h_lyt.addWidget(txt_wgt)
        h_lyt.addWidget(self.buttons_wgt)

        self.setLayout(h_lyt)

        self.tune_ui()

    def enterEvent(self, QEvent):
        #   Shoe edit/delete buttons
        self.buttons_wgt.show()

    def leaveEvent(self, QEvent):
        #   Hide edit/delete buttons
        self.buttons_wgt.hide()

    def delete_entry(self):
        print('Deleted!')

    def edit_entry(self):
        print('Edited')

    """     UI      """
    def tune_ui(self):
        self.setAutoFillBackground(True)

        """     Coloring        """
        if self.my_entry['status'] is not None:
            if self.my_entry['status'] == 1:
                #   Accepted status
                self.setStyleSheet('background-color: {};'.format(self.read_config_file()))
            elif self.my_entry['status'] == 2:
                #   Canceled status
                self.setStyleSheet('background-color: {};'.format(self.read_config_file()))
            else:
                #   Unknown status
                self.setStyleSheet('background-color: {};'.format(self.read_config_file()))
        else:
            #   Default status
            self.setStyleSheet('background-color: {};'.format(self.read_config_file()))

        """     Round corners      """
        """radius = 10
        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), radius, radius)
        mask = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)"""

    def read_config_file(self):
        try:
            file = open('config_files/agenda_entry.json')
            data = json.load(file)
            try:
                #   Return color from config file
                return data[str(self.my_entry['status'])]
            except KeyError as e:
                #   Non existent key
                print('KeyError: Agenda entry', e)
                return '#ABF5B6'
        except FileNotFoundError:
            print('FileNotFoundError: Agenda entry')
            return '#ABF5B6'
        except json.decoder.JSONDecodeError:
            print('No JSON file: Agenda entry')
            return '#ABF5B6'
        """
        #   TODO
        except Exception as e:
            print('Unknown', e, ': Agenda entry')
            return '#ABF5B6'
            # logging.error(traceback.format_exc())
            # Logs the error appropriately.
        """
