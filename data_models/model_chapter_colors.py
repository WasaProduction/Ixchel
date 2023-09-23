class ModelChapterColors:
    def __init__(self, object_id, id_cie, name, color_code):
        self.object_id = object_id
        self.id_cie = id_cie
        self.object_name = name
        # Hexadecimal code
        self.object_color_code = color_code
        self.object_color = "E046A2"

    @property
    def object_id(self):
        return self._object_id

    @object_id.setter
    def object_id(self, value):
        self._object_id = value

    @property
    def id_cie(self):
        return self._id_cie

    @id_cie.setter
    def id_cie(self, value):
        self._id_cie = value

    @property
    def object_name(self):
        return self._object_name

    @object_name.setter
    def object_name(self, value):
        self._object_name = value

    @property
    def object_color_code(self):
        return self._object_color_code

    @object_color_code.setter
    def object_color_code(self, value):
        self._object_color_code = value

    @property
    def object_color(self):
        return self._object_color

    @object_color.setter
    def object_color(self, value):
        self._object_color = value

    def update_object_color(self):
        rgb = []
        for i in (0, 2, 4):
            decimal = int(self.object_color_code[i:i + 2], 16)
            rgb.append(decimal)
        self.object_color = tuple(rgb)

        #self.object_color = Color(self.object_color_code)
