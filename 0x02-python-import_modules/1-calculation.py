#!/usr/bin/python3
from calculator_1 import add, mul, div, sub


def main():
    """Math Operation on a and b"""
    a = 10
    b = 5
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")


if __name__ == "__main__":
    main()
