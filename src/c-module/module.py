# Learning Python 101

import ctypes

class LoadModuleExample:
    def __init__(self):
        self.__module_ = ctypes.CDLL("./module.so")

    def PrintFromCModule(self):
        self.__module_.PrintFromCModule(50)


def main():
    loader = LoadModuleExample()
    loader.PrintFromCModule()

if __name__ == "__main__":
    main()
