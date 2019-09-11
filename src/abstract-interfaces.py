# Learning Python 101

from utils import *
import threading
import time
import random
import abc  # Abstract Base Class - this allows us to define pure virtual methods


class Observer:
    def __init__(self, id):
        self.__id_ = id
        self.__event_ = ""

    def notify(self, event):
        if event != self.__event_:
            printf("Notified Observer ID [" + str(self.__id_) + "] Event: " + event + "\n")
            self.__event_ = event


class SubjectInterface(abc.ABC):
    @abc.abstractmethod  # if we do not implement this method, we get an error during execution
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    @abc.abstractmethod
    def register_observer(self, observer):
        pass


class Subject(SubjectInterface):
    def __init__(self):
        self.__thread_ = threading.Thread(target=self.__run)
        self.__is_running_ = False
        self.__observers_ = []

    def __run(self):
        counter = random.randint(0, 99)
        while self.__is_running_:
            time.sleep(2)
            for observer in self.__observers_:
                observer.notify(str(threading.get_ident()) + "-event-" + str(counter))
            counter += 1

    # Inherited from SubjectInterface
    def start(self):
        self.__is_running_ = True
        self.__thread_.start()

    def stop(self):
        self.__is_running_ = False
        self.__thread_.join()

    def register_observer(self, observer):
        self.__observers_.append(observer)


def main():
    subject_1 = Subject()

    obs_1_1 = Observer(1500)
    obs_1_2 = Observer(1600)

    subject_1.register_observer(obs_1_1)
    subject_1.register_observer(obs_1_2)

    subject_2 = Subject()

    obs_2_1 = Observer(2700)
    obs_2_2 = Observer(2800)

    subject_2.register_observer(obs_2_1)
    subject_2.register_observer(obs_2_2)

    subject_1.start()
    subject_2.start()

    time.sleep(20)

    subject_1.stop()
    subject_2.stop()


if __name__ == "__main__":
    main()
