from PyQt6.QtGui import QTextCharFormat, QTextCursor, QTextDocument, QColor
from mongodb.read.get_color import GetColor


class DiagnosisInfoDoc(QTextDocument):
    def __init__(self, parent=None):
        super().__init__(parent)
        #   Used to apply tints.
        cursor = QTextCursor(self)
        """     Define styles (colors)      """
        #   Default.
        default_format = QTextCharFormat()
        #   Capítulos.
        colors_dict = GetColor().get_colors_dict()
        #   01
        chap_one_format = QTextCharFormat()
        chap_one_format.setForeground(QColor('#' + colors_dict['1']))
        #   02
        chap_two_format = QTextCharFormat()
        chap_two_format.setForeground(QColor('#' + colors_dict['2']))
        #   03
        chap_three_format = QTextCharFormat()
        chap_three_format.setForeground(QColor('#' + colors_dict['3']))
        #   04
        chap_four_format = QTextCharFormat()
        chap_four_format.setForeground(QColor('#' + colors_dict['4']))
        #   05
        chap_five_format = QTextCharFormat()
        chap_five_format.setForeground(QColor('#' + colors_dict['5']))
        #   06
        chap_six_format = QTextCharFormat()
        chap_six_format.setForeground(QColor('#' + colors_dict['6']))
        #   07
        chap_seven_format = QTextCharFormat()
        chap_seven_format.setForeground(QColor('#' + colors_dict['7']))
        #   08
        chap_eight_format = QTextCharFormat()
        chap_eight_format.setForeground(QColor('#' + colors_dict['8']))
        #   09
        chap_nine_format = QTextCharFormat()
        chap_nine_format.setForeground(QColor('#' + colors_dict['9']))
        #   10
        chap_a_format = QTextCharFormat()
        chap_a_format.setForeground(QColor('#' + colors_dict['A']))
        #   11
        chap_b_format = QTextCharFormat()
        chap_b_format.setForeground(QColor('#' + colors_dict['B']))
        #   12
        chap_c_format = QTextCharFormat()
        chap_c_format.setForeground(QColor('#' + colors_dict['C']))
        #   13
        chap_d_format = QTextCharFormat()
        chap_d_format.setForeground(QColor('#' + colors_dict['D']))
        #   14
        chap_e_format = QTextCharFormat()
        chap_e_format.setForeground(QColor('#' + colors_dict['E']))
        #   15
        chap_f_format = QTextCharFormat()
        chap_f_format.setForeground(QColor('#' + colors_dict['F']))
        #   16
        chap_g_format = QTextCharFormat()
        chap_g_format.setForeground(QColor('#' + colors_dict['G']))
        #   17
        chap_h_format = QTextCharFormat()
        chap_h_format.setForeground(QColor('#' + colors_dict['H']))
        #   18
        chap_j_format = QTextCharFormat()
        chap_j_format.setForeground(QColor('#' + colors_dict['J']))
        #   19
        chap_k_format = QTextCharFormat()
        chap_k_format.setForeground(QColor('#' + colors_dict['K']))
        #   20
        chap_l_format = QTextCharFormat()
        chap_l_format.setForeground(QColor('#' + colors_dict['L']))
        #   21
        chap_m_format = QTextCharFormat()
        chap_m_format.setForeground(QColor('#' + colors_dict['M']))
        #   22
        chap_n_format = QTextCharFormat()
        chap_n_format.setForeground(QColor('#' + colors_dict['N']))
        #   23
        chap_p_format = QTextCharFormat()
        chap_p_format.setForeground(QColor('#' + colors_dict['P']))
        #   24
        chap_q_format = QTextCharFormat()
        chap_q_format.setForeground(QColor('#' + colors_dict['Q']))
        #   25
        chap_r_format = QTextCharFormat()
        chap_r_format.setForeground(QColor('#' + colors_dict['R']))
        #   26
        chap_s_format = QTextCharFormat()
        chap_s_format.setForeground(QColor('#' + colors_dict['S']))
        """     Explanation     """
        #   Explanation.
        cursor.insertText("En Ixchel usamos la 11º edición de la codificación internacional de enfermedades (CIE 11), "
                          "para buscar una enfermedad solo comienza a escribir y haremos nuestro mejor para "
                          "recomendarte la mejor opción, ten en cuenta lo siguiente:\n\n"
                          "Debido a que algunas etiquetas están formadas por múltiples palabras, te pedimos sustituir "
                          "los espacios por guiones bajos, de esta manera podemos diferenciar entre enfermedades "
                          "y palabras.\n"
                          "Una enfermedad se convierte en una etiqueta cuando se le aplica un color "
                          "(cada capítulo tiene asignado un color diferente).\n\n", default_format)

        cursor.insertText("\t\tAlgunas_enfermedades_infecciosas_o_parasitarias\n", chap_one_format)
        cursor.insertText("\t\tNeoplasias\n", chap_two_format)
        cursor.insertText("\t\tEnfermedades_de_la_sangre_o_de_los_órganos_hematopoyéticos\n", chap_three_format)
        cursor.insertText("\t\tEnfermedades_del_sistema_inmunitario\n", chap_four_format)
        cursor.insertText("\t\tEnfermedades_endocrinas,_nutricionales_o_metabólicas\n", chap_five_format)
        cursor.insertText("\t\tTrastornos_mentales,_del_comportamiento_y_del_neurodesarrollo\n", chap_six_format)
        cursor.insertText("\t\tTrastornos_del_sueño_y_la_vigilia\n", chap_seven_format)
        cursor.insertText("\t\tEnfermedades_del_sistema_nervioso\n", chap_eight_format)
        cursor.insertText("\t\tEnfermedades_del_sistema_visual\n", chap_nine_format)
        cursor.insertText("\t\tEnfermedades_del_oído_o_de_la_apófisis_mastoides\n", chap_a_format)
        cursor.insertText("\t\tEnfermedades_del_sistema_circulatorio\n", chap_b_format)
        cursor.insertText("\t\tEnfermedades_del_sistema_respiratorio\n", chap_c_format)
        cursor.insertText("\t\tEnfermedades_del_sistema_digestivo\n", chap_d_format)
        cursor.insertText("\t\tEnfermedades_de_la_piel\n", chap_e_format)
        cursor.insertText("\t\tEnfermedades_del_sistema_musculo_esquelético_o_del_tejido\n", chap_f_format)
        cursor.insertText("\t\tEnfermedades_del_sistema_genitourinario\n", chap_g_format)
        cursor.insertText("\t\tCondiciones_relacionadas_con_la_salud_sexual\n", chap_h_format)
        cursor.insertText("\t\tEmbarazo,_parto_o_puerperio\n", chap_j_format)
        cursor.insertText("\t\tAlgunas_afecciones_que_se_originan_en_el_período_perinatal\n", chap_k_format)
        cursor.insertText("\t\tAnomalías_del_desarrollo_prenatal\n", chap_l_format)

        cursor.insertText("\nAl guardar tu diagnóstico, nos encargaremos de tomar estas etiquetas y desplegarlas en el "
                          "resumen del perfil para ti. Gracias.", default_format)
        #   Delimiter.
        #cursor.insertText("\tSeparador", delimiter_format)
        #cursor.insertText(": Valor numérico incremental seguido de un guión, para indicar diferentes instrucciones.\n")
