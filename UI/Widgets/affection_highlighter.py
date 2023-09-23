import re
from PyQt6.QtGui import QColor, QSyntaxHighlighter, QTextCharFormat
from mongodb.mongo_chapter_colors import MongoChapterColors
from mongodb.mongo_affections_vocabulary import MongoAffectionsVocabulary


# https://stackoverflow.com/questions/42677963/how-to-create-tooltip-for-highlighted-strings-in-qplaintextedit
# https://www.youtube.com/watch?v=voUV_WYPxWw
class AffectionHighlighter (QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Retrieve chapter colors from the db
        self.color_dictionary = {}
        for chapter in MongoChapterColors().chapter_colors_obj_array:
            my_color = QColor(chapter.object_color[0], chapter.object_color[1], chapter.object_color[2])
            self.color_dictionary.update({chapter.id_cie[0]: my_color})
        del chapter
        # Database object
        self.mongodb_affections = MongoAffectionsVocabulary()

    def search_affection(self, word):
        self.mongodb_affections.reset_affections_dictionary()
        self.mongodb_affections.set_words(word)
        self.mongodb_affections.retrieve_affection_code()
        return self.mongodb_affections.get_affections_dictionary()

    def set_format(self, affection, text_block):
        pattern_format = QTextCharFormat()
        pattern_format.setFontItalic(True)
        pattern_format.setForeground(self.color_dictionary[affection.id_cie[0]])
        for match in re.finditer(r"\b{}\b".format(affection.name), text_block, re.IGNORECASE):
            start, end = match.span()
            self.setFormat(start, end - start, pattern_format)

    def highlightBlock(self, text_block):
        if len(text_block) > 3:
            ignore_case = re.compile(r'^\w+ *\w+.*$', re.IGNORECASE)
            if re.match(ignore_case, text_block):
                for word in text_block.split():
                    affection = self.search_affection(word)
                    if len(affection) != 0:
                        self.set_format(affection[0], text_block)
            else:
                affection = self.search_affection(''.join(text_block).strip())
                if len(affection) != 0:
                    self.set_format(affection[0], text_block)
            del ignore_case
