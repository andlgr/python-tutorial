# Learning Python 101

# Needs PyQt:
# $ pip3 install PyQt5

from utils import *
import sys
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import abc

class Signal(QObject):
    trigger = pyqtSignal(object, name="trigger")

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
        printf("string - id: " + str(self.__id_) + " - on_signal: " + argument + "\n")


class MyClassWithList(SlotInterface):
    def __init__(self, id):
        super().__init__(id)
        self.__id_ = id

    # Inherited from SlotInterface
    def on_signal(self, argument):
        printf("list - id: " + str(self.__id_) + " - on_signal: ")
        for element in argument:
            printf("[" + element + "] ")
        printf("\n")


def main():
    printf("Playing with signal/slot\n")

    # Emit a string
    slot_1 = MyClass(1)
    slot_2 = MyClass(2)

    signal = Signal()
    signal.trigger.connect(slot_1.on_signal)
    signal.trigger.connect(slot_2.on_signal)

    signal.trigger.emit("I am a string.")

    # Emit a list
    slot_with_list = MyClassWithList(3)

    signal_with_list = Signal()

    signal_with_list.trigger.connect(slot_with_list.on_signal)

    signal_with_list.trigger.emit(["Apple", "Orange", "Grape."])

    signal.trigger.emit("I am another string!")
    signal_with_list.trigger.emit(["I", "am", "another", "list!"])

if __name__ == "__main__":
    main()
