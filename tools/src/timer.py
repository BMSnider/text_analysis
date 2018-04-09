import time


class Timer:
    def __init__(self, subject):
        self.start_time = 0
        self.stop_time = 0
        self.subject = subject
        self.start_error = "Timer not started"
        self.stop_error = "Timer not stopped"

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.stop_time = time.time()

    def duration(self):
        return self.stop_time - self.start_time

    def formatted_time(self):
        duration = self.duration()
        if self.start_time == 0:
            return self.start_error
        if self.stop_time == 0:
            return self.stop_error
        return "{} lasted {} seconds".format(self.subject, duration)
