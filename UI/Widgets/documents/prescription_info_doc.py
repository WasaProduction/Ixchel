from PyQt6.QtGui import QTextCharFormat, QTextCursor, QTextDocument, QColor


class PrescriptionInfoDoc(QTextDocument):
    def __init__(self, parent=None):
        super().__init__(parent)
        #   Used to apply tints.
        cursor = QTextCursor(self)
        """     Define styles (colors)      """
        #   Default.
        default_format = QTextCharFormat()
        #   Delimiter.
        delimiter_format = QTextCharFormat()
        delimiter_format.setForeground(QColor('#f7ab00'))
        #   Drug.
        drug_format = QTextCharFormat()
        drug_format.setForeground(QColor('#010257'))
        #   Hyphen.
        hyphen_format = QTextCharFormat()
        hyphen_format.setForeground(QColor('#ade200'))
        #   Verb.
        verb_format = QTextCharFormat()
        verb_format.setForeground(QColor('#012efc'))
        #   Quantity number.
        quantity_n_format = QTextCharFormat()
        quantity_n_format.setForeground(QColor('#014df5'))
        #   Quantity unit.
        quantity_q_format = QTextCharFormat()
        quantity_q_format.setForeground(QColor('#015ff1'))
        #   Conjunction.
        conjunction_format = QTextCharFormat()
        conjunction_format.setForeground(QColor('#016dee'))
        #   Periodicity number.
        periodicity_n_format = QTextCharFormat()
        periodicity_n_format.setForeground(QColor('#0188e8'))
        #   Periodicity unit.
        periodicity_u_format = QTextCharFormat()
        periodicity_u_format.setForeground(QColor('#01a5e2'))
        #   Preposition.
        preposition_format = QTextCharFormat()
        preposition_format.setForeground(QColor('#01b5df'))
        #   Duration number.
        duration_n_format = QTextCharFormat()
        duration_n_format.setForeground(QColor('#00c9da'))
        #   Duration unit.
        duration_u_format = QTextCharFormat()
        duration_u_format.setForeground(QColor('#00e2d5'))
        #   Semicolon.
        semicolon_format = QTextCharFormat()
        semicolon_format.setForeground(QColor('#ed00ff'))
        #   Indication of use.
        indication_format = QTextCharFormat()
        indication_format.setForeground(QColor('#8cf5e2'))
        """     Insert text with different styles       """
        #   Introduction.
        cursor.insertText("Una prescripción se conforma por una agrupación de instrucciones, a continuación "
                          "puedes encontrar una prescripción y más adelante un desglose detallado.\n\n", default_format)
        """     First instruction      """
        #   Delimiter.
        cursor.insertText("1-\n", delimiter_format)
        #   Drug.
        cursor.insertText("Aspirina", drug_format)
        #   Hyphen.
        cursor.insertText(" - ", hyphen_format)
        #   Verb.
        cursor.insertText("Tomar ", verb_format)
        #   Quantity number.
        cursor.insertText("1 1/2 ", quantity_n_format)
        #   Quantity unit.
        cursor.insertText("pastillas ", quantity_q_format)
        #   Conjunction.
        cursor.insertText("cada ", conjunction_format)
        #   Periodicity number.
        cursor.insertText("8 ", periodicity_n_format)
        #   Periodicity unit.
        cursor.insertText("horas ", periodicity_u_format)
        #   Preposition.
        cursor.insertText("durante ", preposition_format)
        #   Duration number.
        cursor.insertText("7 ", duration_n_format)
        #   Duration unit.
        cursor.insertText("dias ", duration_u_format)
        #   Semicolon.
        cursor.insertText("; ", semicolon_format)
        #   Indication of use.
        cursor.insertText("Acompañar con alimentos.\n", indication_format)

        """     Second instruction      """
        #   Delimiter.
        cursor.insertText("2-\n", delimiter_format)
        #   Drug.
        cursor.insertText("Ventolin", drug_format)
        #   Hyphen.
        cursor.insertText(" - ", hyphen_format)
        #   Verb.
        cursor.insertText("Inhalar ", verb_format)
        #   Quantity number.
        cursor.insertText("1 ", quantity_n_format)
        #   Quantity unit.
        cursor.insertText("disparo ", quantity_q_format)
        #   Conjunction.
        cursor.insertText("cada ", conjunction_format)
        #   Periodicity number.
        cursor.insertText("24 ", periodicity_n_format)
        #   Periodicity unit.
        cursor.insertText("horas ", periodicity_u_format)
        #   Preposition.
        cursor.insertText("durante ", preposition_format)
        #   Duration number.
        cursor.insertText("4 ", duration_n_format)
        #   Duration unit.
        cursor.insertText("meses ", duration_u_format)
        #   Semicolon.
        cursor.insertText("; ", semicolon_format)
        #   Indication of use.
        cursor.insertText("Al presentar malestar.\n", indication_format)

        """     Third instruction       """
        #   Delimiter.
        cursor.insertText("3-\n", delimiter_format)
        #   Drug.
        cursor.insertText("Sensodyne", drug_format)
        #   Hyphen.
        cursor.insertText(" - ", hyphen_format)
        #   Verb.
        cursor.insertText("Aplicar ", verb_format)
        #   Quantity number.
        cursor.insertText("22.6 ", quantity_n_format)
        #   Quantity unit.
        cursor.insertText("g ", quantity_q_format)
        #   Conjunction.
        cursor.insertText("cada ", conjunction_format)
        #   Periodicity number.
        cursor.insertText("24 ", periodicity_n_format)
        #   Periodicity unit.
        cursor.insertText("horas ", periodicity_u_format)
        #   Preposition.
        cursor.insertText("durante ", preposition_format)
        #   Duration number.
        cursor.insertText("22 ", duration_n_format)
        #   Duration unit.
        cursor.insertText("dias ", duration_u_format)
        #   Semicolon.
        cursor.insertText("; ", semicolon_format)
        #   Indication of use.
        cursor.insertText("Antes de dormir.\n", indication_format)

        """     Explanation     """
        #   Explanation.
        cursor.insertText("\nUna instrucción está compuesta de los siguientes elementos:\n\n", default_format)
        #   Delimiter.
        cursor.insertText("\tSeparador", delimiter_format)
        cursor.insertText(": Valor numérico incremental seguido de un guión, para indicar diferentes instrucciones.\n",
                          default_format)
        #   Drug.
        cursor.insertText("\tMedicamento", drug_format)
        cursor.insertText(": Algo.\n", default_format)
        #   Hyphen.
        cursor.insertText("\tGuión", hyphen_format)
        cursor.insertText(": Separador entre medicamento y resto de instrucción.\n", default_format)
        #   Verb.
        cursor.insertText("\tVerbo ", verb_format)
        cursor.insertText(": Accion a realizar.\n", default_format)
        #   Quantity number.
        cursor.insertText("\tCantidad", quantity_n_format)
        cursor.insertText(": Algo.\n", default_format)
        #   Quantity unit.
        cursor.insertText("\tUnidad", quantity_q_format)
        cursor.insertText(": Unidad.\n", default_format)
        #   Conjunction.
        cursor.insertText("\tConjunción", conjunction_format)
        cursor.insertText(": Algo.\n", default_format)
        #   Periodicity number.
        cursor.insertText("\tPeriodicidad", periodicity_n_format)
        cursor.insertText(": Algo.\n", default_format)
        #   Periodicity unit.
        cursor.insertText("\tUnidad de periodicidad", periodicity_u_format)
        cursor.insertText(": Algo.\n", default_format)
        #   Preposition.
        cursor.insertText("\tPreposición", preposition_format)
        cursor.insertText(": Algo.\n", default_format)
        #   Duration number.
        cursor.insertText("\tDuración", duration_n_format)
        cursor.insertText(": Algo.\n", default_format)
        #   Duration unit.
        cursor.insertText("\tUnidad de duración", duration_u_format)
        cursor.insertText(": Algo.\n", default_format)
        #   Semicolon.
        cursor.insertText("\tPunto y coma", semicolon_format)
        cursor.insertText(": Usa ; para dejarnos saber hay instrucciones de uso.\n", default_format)
        #   Indication of use.
        cursor.insertText("\tInstrucción de uso:", indication_format)
        cursor.insertText(" Al redactar te brindaremos un par de opciones frecuentes.\n", default_format)
        #   Conclusion.
        cursor.insertText("\nSeguir este formato nos ayuda a mantener en tu resumen actualizado con todo lo que "
                          "necesitas y en algunos casos, ayudamos a nuestro paciente a seguir un horario bien "
                          "estructurado.", default_format)
