# Learning Python 101

class Reference:
    def __init__(self, param):
        self.__param_ = param
        print("Is the same? " + str(param is self.__param_))

    def change_param(self):
        print("On function - received: " + str(self.__param_[0]))
        self.__param_[0] = 10
        print("On function - changed: " + str(self.__param_[0]))

def main():
    param = [800]
    print("On main - before call: " + str(param[0]))
    obj = Reference(param)
    obj.change_param()
    print("On main - after call: " + str(param[0]))

if __name__ == "__main__":
    main()
