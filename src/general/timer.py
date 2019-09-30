# Learning Python 101

import threading
import time
from utils import *


class MyTimedClass:
    def __init__(self, id, timeout):
        self.__id_ = id
        self.__timeout_ = timeout
        self.__is_running_ = False
        self.__timer_ = threading.Timer(self.__timeout_, self.__on_timer_tick)

    def start(self):
        if not self.__is_running_:
            self.__timer_.start()
            self.__is_running_ = True

    def stop(self):
        if self.__is_running_:
            self.__timer_.cancel()
            self.__is_running_ = False

    def __on_timer_tick(self):
        printf("id: " + str(self.__id_) + " - timer expired after " + str(self.__timeout_) + "s\n")
        if self.__is_running_:
            self.__timer_ = threading.Timer(self.__timeout_, self.__on_timer_tick)
            self.__timer_.start()

def main():
    printf("Timer test\n")

    timer_1 = MyTimedClass(1, 1.0)
    timer_2 = MyTimedClass(2, 0.2)

    timer_1.start()
    timer_2.start()

    time.sleep(5)

    timer_1.stop()
    timer_2.stop()
    printf("Stopped timers\n")

    time.sleep(5)

    printf("Exiting...\n")

if __name__ == "__main__":
    main()
