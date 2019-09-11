# Learning Python 101

import threading
from utils import *


def run(upto):
    for i in range(0, upto):
        printf("[" + str(threading.get_ident()) + "] " + str(i) + "\n")


def main():
    t1 = threading.Thread(target=run, args=(35,))
    t2 = threading.Thread(target=run, args=(20,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
