#!/usr/bin/python3
import sys


def main():

    argv = sys.argv
    len_argv = len(argv) - 1

    if (len_argv == 0):
        print("{} arguments.".format(len_argv))
    elif (len_argv == 1):
        print("{} argument:".format(len_argv))
    else:
        print("{} arguments:".format(len_argv))
        
    for x in range(1, len_argv + 1):
        print("{}: {}".format(x, argv[x]))


if __name__ == "__main__":
    main()
