#!/usr/bin/python3
from calculator_1 import add, mul, div, sub


def main():
    """Math Operation on a and b"""
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))


if __name__ == "__main__":
    main()
