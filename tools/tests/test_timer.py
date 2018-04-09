import unittest
import time
from text_analysis.tools.src.timer import Timer


class TestTimer(unittest.TestCase):
    def setUp(self):
        self.subject = "FISH"

    def test_start(self):
        test = Timer(self.subject)
        test.start()
        self.assertNotEqual(test.start_time, 0)

    def test_end(self):
        test = Timer(self.subject)
        test.stop()
        self.assertNotEqual(test.stop_time, 0)

    def test_duration(self):
        test = Timer(self.subject)
        test.start()
        time.sleep(.001)
        test.stop()
        duration = test.duration()
        self.assertNotEqual(duration, 0)

    def test_formatted_time_start_error(self):
        test = Timer(self.subject)
        result = test.formatted_time()
        self.assertEqual(result, test.start_error)

    def test_formatted_time_stop_error(self):
        test = Timer(self.subject)
        test.start()
        result = test.formatted_time()
        self.assertEqual(result, test.stop_error)

    def test_formatted_time_success(self):
        test = Timer(self.subject)
        test.start()
        time.sleep(.001)
        test.stop()
        duration = test.duration()
        message = "{} lasted {} seconds".format(self.subject, duration)
        self.assertEqual(test.formatted_time(), message)
