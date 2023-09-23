class PatientPeriod:
    def __init__(self, object_id='', first_period='', last_period=None, latest_period=''):
        self.object_id = object_id
        self.first_period = first_period
        self.last_period = last_period
        self.latest_period = latest_period

    """             Getters/Setters             """

    @property
    def object_id(self):
        return self._object_id

    @object_id.setter
    def object_id(self, value):
        self._object_id = value

    @property
    def first_period(self):
        return self._first_period

    @first_period.setter
    def first_period(self, value):
        self._first_period = value

    @property
    def last_period(self):
        return self._last_period

    @last_period.setter
    def last_period(self, value):
        self._last_period = value

    @property
    def latest_period(self):
        return self._latest_period

    @latest_period.setter
    def latest_period(self, value):
        self._latest_period = value
