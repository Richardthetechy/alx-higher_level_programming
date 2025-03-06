#!/usr/bin/python3
import sys


def main():

    argv = sys.argv
    len_argv = len(argv) - 1

    if (len_argv == 1):
        print(f"{len_argv} argument:")
    else:
        print(f"{len_argv} arguments:")

    for x in range(1, len_argv + 1):
        print(f"{x}: {argv[x]}")


if __name__ == "__main__":
    main()
