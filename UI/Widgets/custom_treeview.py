from PyQt6.QtWidgets import QTreeView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from data_models.physical_examination import *
from data_models.physical_examination_entry import *
from data_models.model_vital_signs import *
# https://www.youtube.com/watch?v=LW__NuulfxE


class StandardItem(QStandardItem):
    def __init__(self, txt='', editable=False):
        super().__init__()
        # Prevent edition
        self.setEditable(editable)
        self.setText(txt)


class CustomTreeview(QTreeView):
    def __init__(self, parent=None, arr=None):
        super().__init__(parent=parent)
        vitals = ModelVitalSigns("70 latidos", "40 c", "presion", "ritmo cardiaco", "respiracion", "oxigenacion")
        test_physical_examination = PhysicalExamination(vitals, "Cabeza chueca", "ojos llorosos", "orejas de dumbo",
                                                        "nariz grande", "garganta irritada", "cuello con chupetones")
        test_entry_1 = PhysicalExaminationEntry("Medico_ID", "Patient_ID", "Hoy", "Related_note",
                                                test_physical_examination)
        test_entry_2 = PhysicalExaminationEntry("Medico_IDDDDDD", "Patient_IDDDD", "Ayer", "Related_note",
                                                test_physical_examination)
        my_array = [test_entry_1, test_entry_2]

        #   Change!
        self.arr = my_array #arr

        #   Hide header
        self.setHeaderHidden(True)
        self.tree_model = QStandardItemModel()
        self.root_node = self.tree_model.invisibleRootItem()
        self.tune(self.arr)

    def tune(self, arr=None):
        # One node per entry
        entry_standard_arr = []
        if arr is not None:
            for index, entry in enumerate(arr):
                entry_standard_arr.append(StandardItem(entry['creation_date']))
                vitals = StandardItem('Vitals')
                #   Extract vitals
                for item in entry['content']['vitals'].items():
                    my_str = '{}: {}'.format(item[0], item[1])
                    vitals.appendRow(StandardItem(my_str))
                #   Place vitals under the entry
                entry_standard_arr[index].appendRow(vitals)
                #   Extract exploration data
                for item in list(entry['content'].keys())[1:]:
                    # Exclude None values
                    if entry['content'][item] is not None:
                        my_entry = StandardItem(item)
                        my_entry.appendRow(StandardItem(entry['content'][item]))
                        #   Place items into the entry
                        entry_standard_arr[index].appendRow(my_entry)
                #   Place the entry into the root
                self.root_node.appendRow(entry_standard_arr[index])
            #   Set the model into our tree
            self.setModel(self.tree_model)

    """             Getters/Setters             """
    @property
    def arr(self):
        return self._arr

    @arr.setter
    def arr(self, value):
        self._arr = value
