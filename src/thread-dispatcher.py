# Learning Python 101

import threading
import time
import random
from utils import *


class ThreadDispatcher:
    def __init__(self):
        self.__condition_ = threading.Condition()
        self.__exec_list_ = []
        self.__thread_ = threading.Thread(target=self.__run)
        self.__is_running_ = False

    def get_ident(self):
        return self.__thread_.ident

    def start(self):
        self.__is_running_ = True
        self.__thread_.start()

    def stop(self):
        self.__is_running_ = False
        self.__condition_.acquire()
        self.__condition_.notify()
        self.__condition_.release()
        self.__thread_.join()

    def dispatch(self, method, args):
        if not self.__is_running_:
            return
        self.__condition_.acquire()
        self.__exec_list_.append((method, args))
        self.__condition_.notify()
        self.__condition_.release()

    def __run(self):
        while self.__is_running_:
            self.__condition_.acquire()
            while not self.__exec_list_ and self.__is_running_:
                print("waiting")
                self.__condition_.wait()
            for method, args in self.__exec_list_:
                method(*args)
            self.__exec_list_.clear()
            self.__condition_.release()


class SomeClass:
    def __init__(self, id):
        self.__id_ = id
        self.__thread_dispatcher_ = ThreadDispatcher()

    def start(self):
        self.__thread_dispatcher_.start()

    def stop(self):
        self.__thread_dispatcher_.stop()

    @property
    def __is_thread_safe(self):
        return threading.get_ident() == self.__thread_dispatcher_.get_ident()

    def method_1(self, val1, val2, val3):
        if not self.__is_thread_safe:
            print("method_1: Not thread safe, dispatching...")
            self.__thread_dispatcher_.dispatch(self.method_1,
                                               (val1, val2, val3))
            return

        print("method 1 - id: " + str(self.__id_) + " - " + str(val1), str(val2), str(val3))
        print("Calling method_1 from dispatcher thread:")
        self.method_2(val1, val2, val3)
        print("--------------------------------")

    def method_2(self, val1, val2, val3):
        if not self.__is_thread_safe:
            print("method_2: Not thread safe, dispatching...")
            self.__thread_dispatcher_.dispatch(self.method_2,
                                               (val1, val2, val3))
            return

        print("method 2 - id: " + str(self.__id_)  + " - " + str(val1), str(val2), str(val3))


def some_dispatchable_function(val1, val2, val3):
    print("some dispatchable function: " + str(val1), str(val2), str(val3))


def main():
    printf("Thread Dispatcher\n")

    thread_dispatcher = ThreadDispatcher()
    thread_dispatcher.start()

    for i in range(0, 10):
        # Equivalent to C++ std::bind
        thread_dispatcher.dispatch(some_dispatchable_function,
                                   (i, i + 1 , i + 2))
        if not random.randint(0, 5):
            time.sleep(0.001)

    thread_dispatcher.stop()

    printf("\n\nThread Safety using Thread Dispatcher\n")
    some_class = SomeClass(1)
    some_class.start()

    print("Calling method_1 from main thread:")
    some_class.method_1(1, 2, 3)

    time.sleep(0.5)
    print("")

    print("Calling method_2 from main thread:")
    some_class.method_2(4, 5, 6)

    some_class.stop()


if __name__ == "__main__":
    main()
