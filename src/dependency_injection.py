# Learning Python 101

from utils import *
import random
import abc

class TemperatureDeviceInterface(abc.ABC):
    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    @abc.abstractmethod
    def get_temperature(self) -> int:
        pass


class TemperatureDevice(TemperatureDeviceInterface):
    def __init__(self):
        super().__init__
        self.__is_started_ = False

    # Inherited from TemperatureDeviceInterface
    def start(self):
        self.__is_started_ = True

    def stop(self):
        self.__is_started_ = False

    def get_temperature(self) -> float:
        return round(random.uniform(-200, 200), 2)


class InvalidTemperatureDevice():
    def __init__(self):
        super().__init__
        self.__is_started_ = False

    # Inherited from TemperatureDeviceInterface
    def start(self):
        self.__is_started_ = True

    def stop(self):
        self.__is_started_ = False

    def get_temperature(self) -> float:
        return round(random.uniform(-200, 200), 2)


class Controller:
    def __init__(self, device):  # Must be passed as list in order to keep reference
        if not isinstance(device, list):
            raise Exception("Please pass object inside a list in order to keep reference inside Controller")
        if not isinstance(device[0], TemperatureDeviceInterface):
            raise Exception("Invalid device object type, please inherit from TemperatureDeviceInterface")
        self.__device_ = device

    def start(self):
        self.__device_[0].start()

    def stop(self):
        self.__device_[0].stop()

    def print_temperature(self):
        printf("Temperature: " + str(self.__device_[0].get_temperature()) + " oC\n")

    def get_temperature(self) -> float:
        return self.__device_[0].get_temperature()


def main():
    device = [TemperatureDevice()]
    controller = Controller(device)
    controller.print_temperature()

    try:
        # Not inherited from TemperatureDeviceInterface - should raise an exception
        invalid_device = [InvalidTemperatureDevice()]
        invalid_controller = Controller(invalid_device)
        invalid_controller.print_temperature()
    except Exception as err:
        printf("Cannot create controller: " + str(err) + "\n")

    try:
        # Not passing as list - should raise an exception
        device = TemperatureDevice()
        controller = Controller(device)
        controller.print_temperature()
    except Exception as err:
        printf("Cannot create controller: " + str(err) + "\n")

if __name__ == "__main__":
    main()
