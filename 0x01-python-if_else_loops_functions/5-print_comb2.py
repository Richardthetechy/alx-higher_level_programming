#!/usr/bin/python3

for x in range(0, 100):
    if x == 99:
        print(x)
    else:
        print("{num:02d}, ".format(num=x), end="")
