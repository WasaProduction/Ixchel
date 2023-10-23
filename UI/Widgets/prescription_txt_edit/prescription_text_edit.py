#   For Text Edit
from PyQt6.QtWidgets import QPlainTextEdit
#   For completer
from UI.Widgets.prescription_txt_edit.drug_completer import DrugCompleter
from PyQt6.QtWidgets import QCompleter
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextCursor
#   For highlighter
from spell_check import SpellCheck
from UI.Widgets.prescription_txt_edit.drug_highlighter import DrugHighlighter
#   Prescription vocabulary
from mongodb.read.get_prescription_vocabulary import GetPrescriptionVocabulary
#   Using regex
import re
#   Fractions
#   Uncomment for future need of processing fractions
# from format_converter.str_fractions import StrFractions
#   Instructions
from data_models.prescriptions.model_treatment import *


#   TODO
#   https://forum.qt.io/topic/13677/adding-a-tooltip-in-qplaintextedit/4
#   https://stackoverflow.com/questions/42677963/how-to-create-tooltip-for-highlighted-strings-in-qplaintextedit
class PrescriptionTextEdit(QPlainTextEdit):
    def __init__(self, parent=None, chk_dict_path='', placeholder_str=None, contained_str='1-\n'):
        super(PrescriptionTextEdit, self).__init__(parent)
        self.document()
        #   Completer
        self.drugs_vocabulary = ['Advil', 'Australopithecus']
        #   Verbs, units
        self.prescription_vocabulary = GetPrescriptionVocabulary()
        self.completer_dict = []
        self.completer = DrugCompleter(self)
        self.completer.setWidget(self)
        self.completer.insertText.connect(self.insert_completion)
        #   Checker
        self.checker = SpellCheck(chk_dict_path)
        #   Highlighter
        self.highlighter = DrugHighlighter()
        self.set_up_editor()
        if placeholder_str is not None:
            self.setPlaceholderText('Placeholder')
        else:
            self.setPlaceholderText('This is an example')
        if contained_str is not None:
            self.insertPlainText(contained_str)
        self.tune_ui()
        #   for processing Data
        self.my_lines = []

    """     Completer block     """

    def update_completer_model(self, new_dictionary):
        self.completer.update_dictionary(new_dictionary)

    def focusInEvent(self, event):
        if self.completer:
            self.completer.setWidget(self)
        QPlainTextEdit.focusInEvent(self, event)

    def insert_completion(self, completion):
        tc = self.textCursor()
        # Get the remaining characters missing of the word to complete
        extra = (len(completion) - len(self.completer.completionPrefix()))
        tc.movePosition(QTextCursor.MoveOperation.Left)
        tc.movePosition(QTextCursor.MoveOperation.EndOfWord)
        # Insert those characters at the end of the word
        tc.insertText(completion[-extra:])
        self.setTextCursor(tc)
        self.completer.popup().hide()

    #   Insert numeration (delimiter)
    def insert_number(self):
        tc = self.textCursor()
        #   Delimiter is composed of 'number-\n' where number increases by 1.
        #   Validate previous line isn't a delimiter already.
        try:
            previous_text = self.document().toPlainText().strip()[:tc.position()]
            #   Look for last 2 characters.
            if re.match(r'\d+-', previous_text[-2:]):
                #   Delimiter format.
                return
        except IndexError:
            #   -2 position is non existent.
            return
        #   Validate cursor is at the end of block.
        pos = tc.positionInBlock()
        tc.select(QTextCursor.SelectionType.BlockUnderCursor)
        if pos + 1 < len(tc.selectedText()):
            #   return if position is in the middle of a string.
            return
        else:
            #   Refresh cursor
            tc = self.textCursor()
            #   One extra space for visual concerns.
            delimiter = ''.join(['\n\n', str(len(self.find_instructions()) + 1), '-'])
            #   Move position to the end of word.
            tc.movePosition(QTextCursor.MoveOperation.EndOfWord)
            # Insert delimiter  at the end of the word.
            tc.insertText(delimiter)
            self.setTextCursor(tc)

    def process_text(self):
        #   Retrieve cursor.
        tc = self.textCursor()
        #   Select current cursor text block.
        tc.select(QTextCursor.SelectionType.BlockUnderCursor)
        #   Completer contents.
        #   Check if there is a -
        if '-' in tc.selectedText():
            #   Drug has been redacted.
            #   Determine.
            completer_contents = self.text_post_drug(tc, tc.selectedText())
        else:
            #   Drug is being redacted.
            completer_contents = self.drugs_vocabulary
        #   Update completer.
        self.update_completer_model(completer_contents)

    """     Text edit block      """
    def keyPressEvent(self, event):
        tc = self.textCursor()

        #   Key events
        enter_return = event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter
        #   Autocomplete if tab or enter is pressed and completer  visible
        if (event.key() == Qt.Key.Key_Tab or enter_return) and self.completer.popup().isVisible():
            self.completer.insertText.emit(self.completer.get_selected())
            self.completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
            return

        #   Insert numerated delimiters
        if enter_return:
            self.insert_number()

        #   Autocomplete brackets
        self.autocomplete_brackets(event, tc)

        QPlainTextEdit.keyPressEvent(self, event)
        tc.select(QTextCursor.SelectionType.WordUnderCursor)
        cr = self.cursorRect()

        if len(tc.selectedText()) > 0:
            self.process_text()
            self.completer.setCompletionPrefix(tc.selectedText())
            popup = self.completer.popup()
            popup.setCurrentIndex(self.completer.completionModel().index(0, 0))

            cr.setWidth(self.completer.popup().sizeHintForColumn(0)
                        + self.completer.popup().verticalScrollBar().sizeHint().width())
            self.completer.complete(cr)
        else:
            self.completer.popup().hide()

    def autocomplete_brackets(self, event, cursor):
        # options = {"(": ")", "[": "]", "{": "}"}
        #   Return value assigned to each value
        options = {"(": ")"}
        option = options.get(event.text())
        #   Insert value if exist
        if option is not None:
            #   Cursor current position
            p = cursor.position()
            #   Insert value
            self.insertPlainText(option)
            cursor.setPosition(p)
            self.setTextCursor(cursor)
            return True

    @staticmethod
    def number_positions(input_string):
        #   List for coordinates
        number_positions = []
        #   Regex to be used
        pattern = r'[-+]?\d+\.?\d*|\d*\.?\d+'
        #   Find all numbers (decimal, rational, rational + whole)
        for match in re.finditer(pattern, input_string):
            start_pos = match.start()
            end_pos = match.end()
            #   Merge numbers if separated by slight separation (for '.', ' ', and '/')
            if len(number_positions):
                #   Retrieve previous coordinates
                prev_start, prev_end = number_positions[-1]
                #   Compare last ending with current start
                if (start_pos - prev_end) <= 1:
                    #   Update last entry with new ending
                    number_positions[-1] = (prev_start, end_pos)
                else:
                    #   Add new entry
                    number_positions.append((start_pos, end_pos))
            else:
                #   Add new entry
                number_positions.append((start_pos, end_pos))
        return number_positions

    @staticmethod
    def brackets_positions(text):
        #   Find brackets coordinates
        for m in re.finditer(r'.*\(.*\)', text):
            return m.start(), m.end()
        return None, None

    """     Retrieve data       """
    def drug_redacted(self, cursor, text):
        #   Retrieve cursor position
        cursor_position = cursor.positionInBlock()
        """     Redacting instruction       """
        #   If parenthesis is not present (thus no drug) return
        if '-' not in text:
            return
        else:
            #   Split instruction from drug
            sentence = text.split(')')
            #   Update position without drug
            cursor_position -= len(sentence[0])
            #   If there's indeed an instruction to be processed
            if len(sentence) > 1:
                #   Update instruction for further processing
                instruction = sentence[1].strip() if sentence[1].strip() is not None else ''
            else:
                #   No text yet after drug
                return
            #   Deduct part being redacted
            return self.redacting_instruction(instruction, len(self.document().toPlainText()))

    def text_post_drug(self, cursor, text):
        #   Retrieve cursor position
        cursor_position = cursor.positionInBlock()
        """     Redacting instruction       """
        #   Split instruction from drug
        sentence = text.split('-')
        #   Update position without drug
        cursor_position -= len(sentence[0])
        #   If there's indeed an instruction to be processed
        if len(sentence) > 1:
            #   Update instruction for further processing
            instruction = sentence[1].strip() if sentence[1].strip() is not None else ''
        else:
            #   No text after drug
            return []
        #   Deduct part being redacted
        return self.redacting_instruction(instruction, cursor_position)

    def redacting_instruction(self, instruction, cursor_position):
        #   Find all numbers to base our deduction
        number_positions = self.number_positions(instruction)
        #   Discard cursor position inversely
        if len(number_positions) >= 3:
            start, end = number_positions[2]
            if end < cursor_position:
                if ';' in instruction:
                    #   Indication for use being redacted
                    return self.prescription_vocabulary.indication_use
                else:
                    #   Duration being redacted
                    return self.prescription_vocabulary.duration_units

        if len(number_positions) >= 2:
            start, end = number_positions[1]
            if end < cursor_position:
                if len(instruction[end:].split()) > 1:
                    #   Preposition being redacted
                    return self.prescription_vocabulary.prepositions
                else:
                    #   Periodicity being redacted
                    return self.prescription_vocabulary.dosage_units

        if len(number_positions) >= 1:
            start, end = number_positions[0]
            if end < cursor_position:
                if len(instruction[end:].split()) > 1:
                    #   Preposition being redacted
                    return self.prescription_vocabulary.prepositions
                else:
                    #   Dose being redacted
                    return self.prescription_vocabulary.dose_units

        if len(number_positions) >= 0:
            #   Action being redacted
            return self.prescription_vocabulary.actions

    """     Highlighter Block       """
    def set_up_editor(self):
        self.highlighter.setDocument(self.document())

    """     Process Data       """
    def retrieve_data(self):
        #   Check if there's text to consume
        if not self.document().toPlainText().strip():
            return None
        #   Look for instructions delimiters (number-) and clean possible errors
        delimiters = self.find_instructions()
        #   Interpret instructions
        if delimiters:
            #   Merge previously separated lines into blocks
            my_instructions = self.merge_multiline_instructions(delimiters)
            #   Digest each block as an instruction.
            """
            for instruction in my_instructions:
                print(self.digest_instructions(instruction))
            """
            return self.digest_instructions(my_instructions)
        else:
            #   Filter out empty delimiter
            if re.match(r'\d+-', self.document().toPlainText().strip()):
                return None
            #   Try to process paragraph as instruction
            possible_instruction = self.digest_based_on_type(self.document().toPlainText().strip())
            try:
                if possible_instruction['raw_text']:
                    return possible_instruction
                else:
                    return self.document().toPlainText().strip()
            except KeyError:
                #   No discernible text
                #   TODO
                return None

    def find_instructions(self):
        #   Break text by lines while omitting empty ones
        self.my_lines = [line for line in self.document().toPlainText().split('\n') if line.strip()]
        #   Count number lines
        delimiters = []
        empty_delimiters = []
        for index, line in enumerate(self.my_lines):
            #   Filter out empty delimiters.
            try:
                if re.match(r'\d+-', line) and re.match(r'[a-zA-Z()]+', self.my_lines[index + 1]):
                    #   Number followed by words
                    delimiters.append(index)
                elif re.match(r'\d+-', line) and re.match(r'\d+-', self.my_lines[index + 1]):
                    #   Number followed by number.
                    empty_delimiters.append(index)
            except IndexError:
                #   Remove last empty separator from global list.
                empty_delimiters.append(index)

        #   Remove empty delimiters
        if empty_delimiters:
            for index in reversed(empty_delimiters):
                #   Update delimiter position
                for i, delimiter in enumerate(delimiters):
                    if index < delimiter:
                        #   -1 if anything before delimiter position is removed
                        delimiters[i] = delimiter - 1
                self.my_lines.pop(index)
        return delimiters

    def merge_multiline_instructions(self, delimiters):
        #   Copy lines to prevent errors
        instruction_array = self.my_lines
        processed_array = []
        #   Iterate reversed for simplicity.
        for separator in reversed(delimiters):
            #   Join all the text after the delimiter and return \n.
            processed_array.append('\n'.join(instruction_array[separator + 1:]))
            #   Get rid of the text beyond the delimiter (including itself).
            instruction_array = instruction_array[:separator]
        #   Return the list back to the original order.
        return list(reversed(processed_array))

    def digest_instructions(self, instructions):
        orders = []
        #   Multiple instructions
        if type(instructions) == list:
            for instruction in instructions:
                orders.append(self.digest_based_on_type(instruction))
        #   Single instruction
        elif type(instructions) == str:
            orders.append(self.digest_based_on_type(instructions))
        return orders

    def digest_based_on_type(self, instruction):
        #   Intended to digest single instruction
        #   Prepare Instruction obj
        instruction_obj = self.identify_instruction_type(instruction)
        if instruction_obj is None:
            return None
        elif instruction_obj['instruction_type'] == 0:
            #   Only drug
            return self.digest_0_part(instruction_obj)
        elif instruction_obj['instruction_type'] <= 1:
            #   0 Number instruction
            #   Either contain
            return self.digest_0_part(instruction_obj)
        elif instruction_obj['instruction_type'] <= 2:
            #   1 Number instruction
            return self.digest_1_part(instruction_obj)
        elif instruction_obj['instruction_type'] <= 3:
            #   2 Number instruction
            return self.digest_2_part(instruction_obj)
        elif instruction_obj['instruction_type'] <= 4:
            #   3 Number instruction
            return self.digest_3_part(instruction_obj)

    def identify_instruction_type(self, instruction):
        instruction_obj = Instruction()
        instruction_obj['raw_text'] = instruction

        """     Break down basic structure: Drug - Instruction      """
        #   First text inside brackets is to be the drug
        # instruction_obj['drug'] = re.findall(r'\((.*?)\)', instruction)[0]
        #   Instruction should start with drug followed by -
        if '-' in instruction:
            instruction_obj['drug'] = instruction.split('-')[0]
        #   To locate remaining text
        closing_bracket = instruction.find(')')
        if closing_bracket > 0:
            text_after = ''.join(instruction[closing_bracket + 1:])
        else:
            #   No drug
            text_after = instruction

        """     Break down instruction: Instruction; Use case. Complement       """
        if text_after:
            #   Remove blank spaces
            clean_text = text_after.strip()
            #   Use case exist
            if ';' in clean_text:
                split_txt = clean_text.split(';')
                instruction_obj['instruction'] = split_txt[0]
                #   Compliment exist
                if '\n' in split_txt[0]:
                    temp = split_txt[0].split('\n')
                    instruction_obj['indication_of_use'] = temp[0]
                    instruction_obj['complement'] = temp[1]
                else:
                    #   No compliment
                    instruction_obj['indication_of_use'] = split_txt[1]
            else:
                # TODO further develop scenario
                # No use_case only 1 line compliment
                instruction_obj['complement'] = clean_text
                instruction_obj['instruction_type'] = 1
                return instruction_obj
        else:
            #   Only drug no instruction
            #   TODO further develop scenario
            instruction_obj['instruction_type'] = 0
            return instruction_obj

        """     Testing     """
        """
        print('-------------------------------------------')
        print('Instruction obj test:\nDrug:\n', test_instruction['drug'])
        print('Instruction:', test_instruction['instruction'])
        print('Indication of use:\n', test_instruction['indication_of_use'])
        print('Complement:\n', test_instruction['complement'])
        print('-------------------------------------------')
        """

        """     Instruction types classified by the amount of numbers        """
        if instruction_obj['instruction']:
            number_pos = self.number_positions(instruction_obj['instruction'])
        else:
            #   No instruction
            instruction_obj['instruction_type'] = 0
            return instruction_obj

        if len(number_pos) == 3:
            instruction_obj['instruction_type'] = 4
            return instruction_obj
        elif len(number_pos) == 2:
            instruction_obj['instruction_type'] = 3
            return instruction_obj
        elif len(number_pos) == 1:
            instruction_obj['instruction_type'] = 2
            return instruction_obj
        #   No case applies
        return None

    def digest_3_part(self, instruction_obj):
        """     3 Part instruction      """
        #   Extract position of the numbers contained
        number_positions = self.number_positions(instruction_obj['instruction'])

        """        Quantity     """
        #   First number is supposed to be quantity
        number_start, number_end = number_positions[0]
        quantity = instruction_obj['instruction'][number_start:number_end]
        #   The quantity should be followed by its unit
        #   TODO validate quantity units & StrFractions
        quantity_unit = instruction_obj['instruction'][number_end:].split()[0]
        #   Assign values to Quantity obj and that into Instruction obj
        instruction_obj['quantity'] = Quantity(quantity, quantity_unit)

        """     Periodicity     """
        #   Second number is supposed to be the periodicity
        number_start, number_end = number_positions[1]
        periodicity = instruction_obj['instruction'][number_start:number_end]
        #   The periodicity should be followed by its unit
        #   TODO validate periodicity units & StrFractions
        periodicity_unit = instruction_obj['instruction'][number_end:].split()[0]
        #   Assign values to Quantity obj and that into Instruction obj
        instruction_obj['periodicity'] = Quantity(periodicity, periodicity_unit)

        """     Duration        """
        #   Third number is supposed to be the duration
        number_start, number_end = number_positions[2]
        duration = instruction_obj['instruction'][number_start:number_end]
        #   The duration should be followed by its unit
        #   TODO validate duration units & StrFractions
        duration_unit = instruction_obj['instruction'][number_end:].split()[0]
        #   Assign values to Quantity obj and that into Instruction obj
        instruction_obj['duration'] = Quantity(duration, duration_unit)

        #   Testing
        #self.testing_returned_obj(instruction_obj)
        return instruction_obj

    def digest_2_part(self, instruction_obj):
        """     2 Part instruction      """
        #   Extract position of the numbers contained
        number_positions = self.number_positions(instruction_obj['instruction'])

        """        Quantity     """
        #   First number is supposed to be quantity
        number_start, number_end = number_positions[0]
        quantity = instruction_obj['instruction'][number_start:number_end]
        #   The quantity should be followed by its unit
        #   TODO validate quantity units & StrFractions
        quantity_unit = instruction_obj['instruction'][number_end:].split()[0]
        #   Assign values to Quantity obj and that into Instruction obj
        instruction_obj['quantity'] = Quantity(quantity, quantity_unit)

        """     Duration        """
        #   Third number is supposed to be the duration
        number_start, number_end = number_positions[1]
        duration = instruction_obj['instruction'][number_start:number_end]
        #   The duration should be followed by its unit
        #   TODO validate duration units & StrFractions
        duration_unit = instruction_obj['instruction'][number_end:].split()[0]
        #   Assign values to Quantity obj and that into Instruction obj
        instruction_obj['duration'] = Quantity(duration, duration_unit)

        #   Testing
        self.testing_returned_obj(instruction_obj)
        return instruction_obj

    def digest_1_part(self, instruction_obj):
        """     1 Part instruction      """
        #   Extract position of the numbers contained
        number_positions = self.number_positions(instruction_obj['instruction'])

        #   Single line
        """        Quantity     """
        #   First number is supposed to be quantity
        number_start, number_end = number_positions[0]
        quantity = instruction_obj['instruction'][number_start:number_end]
        #   The quantity should be followed by its unit
        #   TODO validate quantity units & StrFractions
        quantity_unit = instruction_obj['instruction'][number_end:].split()[0]
        #   Assign values to Quantity obj and that into Instruction obj
        instruction_obj['quantity'] = Quantity(quantity, quantity_unit)

        #   Testing
        # self.testing_returned_obj(instruction_obj)
        return instruction_obj

    def digest_0_part(self, instruction_obj):
        """     0 Part instruction      """
        #   No numbers
        #   Testing
        self.testing_returned_obj(instruction_obj)
        return instruction_obj

    @staticmethod
    def testing_returned_obj(instruction_obj):
        """     Testing     """
        print('-------------------------------------------')
        print('Raw text:', instruction_obj['raw_text'])
        if instruction_obj['drug'] is not None:
            print('Drug:', instruction_obj['drug'])
        if instruction_obj['quantity']['quantity'] is not None:
            print('Qty:', instruction_obj['quantity']['quantity'], 'Unit:', instruction_obj['quantity']['unit'])
        if instruction_obj['periodicity']['quantity'] is not None:
            print('Periodicity:', instruction_obj['periodicity']['quantity'], 'unit:', instruction_obj['periodicity'][
                'unit'])
        if instruction_obj['duration']['quantity'] is not None:
            print('Duration:', instruction_obj['duration']['quantity'], 'unit:', instruction_obj['duration']['unit'])
        if instruction_obj['indication_of_use'] is not None:
            print('Indication of use:', instruction_obj['indication_of_use'])
        if instruction_obj['complement'] is not None:
            print('Complement', instruction_obj['complement'])
        print('-------------------------------------------')

    """     UI      """
    def tune_ui(self):
        # self.setMinimumWidth()
        # self.setMaximumWidth()
        self.setMinimumHeight(200)
        # self.setMaximumHeight()
