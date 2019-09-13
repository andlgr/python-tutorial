# Learning Python 101

class ClassWithReferenceToDependency:
    def __init__(self, param):
        if not isinstance(param, list):
            raise Exception(
                "Please pass object inside a list in order to keep reference inside ClassWithReferenceToDependency")
        self.__param_ = param  # A mutable type like list behaves like a shared_ptr in C++. To copy, use param.copy()
        print("Is the same? " + str(param is self.__param_))

    def change_param(self):
        print("change_param - current: " + str(self.__param_[0]))
        self.__param_[0] = 10
        print("change_param - changed: " + str(self.__param_[0]))


def main():
    param = [800]
    print("On main - before call: " + str(param[0]))
    obj = ClassWithReferenceToDependency(param)
    obj.change_param()
    print("On main - after call: " + str(param[0]))
    assert(10 == param[0])


if __name__ == "__main__":
    main()
