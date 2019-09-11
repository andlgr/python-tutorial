# Learning Python 101

import functools

printf = functools.partial(print, end="")


def main():
    print("Do not execute this module directly")


if __name__ == "__main__":
    main()
