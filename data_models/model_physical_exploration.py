"""
For Physical exploration model
Classes:
    ModelPhysicalExploration
NOM-004-SSA3-2012
6.1.1 Interrogatorio.- Deberá tener como mínimo: ficha de identificación, en su caso, grupo étnico, antecedentes heredo-familiares, antecedentes personales patológicos (incluido uso y dependencia del tabaco, del alcohol y de otras sustancias psicoactivas, de conformidad con lo establecido en la Norma Oficial Mexicana, referida en el numeral 3.12 de esta norma) y no patológicos, padecimiento actual (indagar acerca de tratamientos previos de tipo convencional, alternativos y tradicionales) e interrogatorio por aparatos y sistemas;
"""


class ModelPhysicalExploration:
    def __init__(self, object_id='', first_period='', last_period=None, latest_period=''):
        self.object_id = object_id
        self.first_period = first_period
        self.last_period = last_period
        self.latest_period = latest_period
