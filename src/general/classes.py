# Learning Python 101

from utils import *  # Must be careful when importing everything (*)

class MyFirstClass:
    # Constructor
    def __init__(self, name, age):
        self.__name_ = name  # '__' indicates private member
        self.__age_ = age  # '__' indicates private member

    def print_info(self):  # Every method has to receive 'self'
        printf("Name: " + self.__name_)
        printf("\nAge: " + str(self.__age_))

    def get_name(self) -> str:  # annotate return type, also forcing conversion
        return self.__name_


class MyFirstInheritance(MyFirstClass):
    pass  # Use the 'pass' keyword when you do not want to add any other properties or methods to the class.


class MySecondClass(MyFirstInheritance):
    def __init__(self, name, age, profession):
        super().__init__(name, age)  # calls method from parent - equivalent to virtual ctor in C++
        self.__profession_ = profession

    def print_info(self):  # method override
        super().print_info()
        printf("\nProfession: " + self.__profession_)


def main():  # implicit '-> None', equivalent to C/C++ void return
    printf("Hello World!\n\n")

    # Objects creation
    andre    = MyFirstClass("Andre R.", 30)
    ulrich   = MyFirstInheritance("Tothor R.", 20)
    engineer = MySecondClass("Reis", 30, "Computer Engineer")

    andre.print_info()
    printf("\n\n")

    ulrich.print_info()
    printf("\n\n")

    engineer.print_info()
    printf("\n\n")

    printf(andre.get_name())
    printf("\n\n")

# Only execute main() if this file is launched through terminal
if __name__ == "__main__":
    main()
