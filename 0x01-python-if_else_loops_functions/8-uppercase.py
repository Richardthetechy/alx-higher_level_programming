#!/usr/bin/python3

def uppercase(str):
    text = ""
    length = len(str)

    for x in range(0, length):
        if 'a' <= str[x] <= 'z':
            text += chr(ord(str[x]) - 32)
        else:
            text += str[x]
    print(text)