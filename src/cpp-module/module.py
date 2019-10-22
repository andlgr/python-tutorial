# Learning Python 101

import time
import build.module  # Our C++ shared library is located at ./build/module.so

def callback(obj):
    print("called back")

def main():
    dispatcher = build.module.Dispatcher()
    #time.sleep(2)
    dispatcher.SetCallback(callback)
    while (True):
        time.sleep(5)
    # printer = build.module.MyPrinter()
    # cpp_obj = build.module.MyModule()
    #
    # cpp_obj.PrintFromCppModule(80)
    # cpp_obj.PrintFromOtherObject(printer)  # 'printer' is being passed as pointer
    #
    # print("Now printing from python:")
    # printer.Print()
    # cpp_obj.PrintFromOtherObject(printer)
    # cpp_obj.PrintFromOtherObject(None)  # Equivalent to nullptr
    # printer.Print()
    # printer.Print()
    #
    # printer_2 = printer  # Doesn't copy - equivalent to reference
    # cpp_obj.PrintFromOtherObject(printer)
    # cpp_obj.PrintFromOtherObject(printer)
    # cpp_obj.PrintFromOtherObject(printer)
    # cpp_obj.PrintFromOtherObject(printer_2)
    #
    # printer = None  # Sets to nullptr
    # cpp_obj.PrintFromOtherObject(printer)
    # cpp_obj.PrintFromOtherObject(printer_2)


if __name__ == "__main__":
    main()
