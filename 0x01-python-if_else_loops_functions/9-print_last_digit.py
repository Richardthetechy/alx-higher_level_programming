#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        lastDigit = (10 - (number % 10))
    else:
        lastDigit = number % 10
    return lastDigit
