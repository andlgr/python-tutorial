# Learning Python 101

# Needs PyQt:
# $ pip3 install PyQt5

from utils import *
import sys
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import abc

class Signal(QObject):
    trigger = pyqtSignal(object, name="trigger")  # Mandatory to be outside ctor (why?)

    def __init__(self):
        super().__init__()


class SlotInterface(QObject):
    def __init__(self, id):
        super().__init__()
        self.__id_ = id

    @abc.abstractmethod
    @pyqtSlot(object)  # 'object' is a generic way of decorating a slot
    def on_signal(self, argument):
        pass


class MyClass(SlotInterface):
    def __init__(self, id):
        super().__init__(id)
        self.__id_ = id

    # Inherited from SlotInterface
    def on_signal(self, argument):
        if not isinstance(argument, str):
            printf("id: " + str(self.__id_) + " - Error: invalid type while executing on_signal - not a string\n")
            return
        printf("string - id: " + str(self.__id_) + " - on_signal: " + argument + "\n")


class MyClassWithList(SlotInterface):
    def __init__(self, id):
        super().__init__(id)
        self.__id_ = id

    # Inherited from SlotInterface
    def on_signal(self, argument):
        if not isinstance(argument, list):
            printf("id: " + str(self.__id_) + " - Error: invalid type while executing on_signal - not a list\n")
            return
        printf("list - id: " + str(self.__id_) + " - on_signal: ")
        for element in argument:
            printf("[" + element + "] ")
        printf("\n")


def main():
    printf("Playing with signal/slot\n")

    # Test for string
    slot_1 = MyClass(1)
    slot_2 = MyClass(2)

    signal_with_string = Signal()
    signal_with_string.trigger.connect(slot_1.on_signal)
    signal_with_string.trigger.connect(slot_2.on_signal)

    # Test for list
    slot_with_list = MyClassWithList(3)

    signal_with_list = Signal()
    signal_with_list.trigger.connect(slot_with_list.on_signal)

    # Emit
    signal_with_string.trigger.emit("I am a string.")
    signal_with_list.trigger.emit(["Apple", "Orange", "Grape."])
    signal_with_string.trigger.emit("I am another string!")
    signal_with_list.trigger.emit(["I", "am", "another", "list!"])

    # Emit invalid
    signal_with_string.trigger.emit(["I", "shall", "not", "get", "printed!"])
    signal_with_list.trigger.emit("I shall not get printed too!")

if __name__ == "__main__":
    main()
