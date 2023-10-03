from PyQt6.QtCore import QTimer


class ThrottleDebounce:
    def __init__(self, task=None):
        #   Code to execute
        self.task = task
        # Throttle and debounce timers
        self.throttle_timer = QTimer()
        self.debounce_timer = QTimer()

        # Set the time interval for throttle and debounce (in milliseconds)
        self.throttle_interval = 1000  # 1 second
        self.debounce_interval = 1000  # 1 second

        # Connect timer timeouts to the respective functions
        self.throttle_timer.timeout.connect(self.throttle_task)
        self.debounce_timer.timeout.connect(self.debounce_task)

        # Initialize flags to track button clicks
        self.throttle_flag = False
        self.debounce_flag = False

    def throttle(self):
        if not self.throttle_flag:
            self.throttle_flag = True
            self.throttle_timer.start(self.throttle_interval)

    def debounce(self):
        self.debounce_flag = True
        self.debounce_timer.stop()
        self.debounce_timer.start(self.debounce_interval)

    def throttle_task(self):
        print('Throttle')
        #   Throttle action executed
        self.task()
        self.throttle_flag = False
        self.throttle_timer.stop()

    def debounce_task(self):
        print('debounce')
        if self.debounce_flag:
            #   Debounce action executed
            self.task()
            self.debounce_flag = False


