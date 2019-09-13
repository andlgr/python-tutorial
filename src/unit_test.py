# Learning Python 101

import unittest
import mock
from utils import *
from dependency_injection import *

# I am going to test Controller class from 'dependency_injection.py'.
# For that, I am going to define a MockedTemperatureDevice and inject
# on Controller, so I can check its behavior.

class ControllerTest(unittest.TestCase):
    def test_get_temperature(self):
        test_value = 300.0

        # DUT dependency + Mock setup
        device = [TemperatureDevice()]
        device[0].get_temperature = mock.MagicMock(return_value=test_value)

        # DUT
        controller = Controller(device)

        # Test and check
        self.assertEqual(test_value, controller.get_temperature())

        # Expectation
        device[0].get_temperature.assert_called()

    def test_start(self):
        # DUT dependency + Mock setup
        device = [TemperatureDevice()]
        device[0].start = mock.MagicMock()

        # DUT
        controller = Controller(device)

        # Test and check
        controller.start()

        # Expectation
        device[0].start.assert_called_once()

    def test_stop(self):
        # DUT dependency + Mock setup
        device = [TemperatureDevice()]
        device[0].stop = mock.MagicMock()

        # DUT
        controller = Controller(device)

        # Test and check
        controller.stop()

        # Expectation
        device[0].stop.assert_called_once()


if __name__ == '__main__':
    unittest.main()
