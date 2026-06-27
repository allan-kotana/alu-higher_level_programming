#!/usr/bin/python3
def uppercase(str):
    up = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            up += "{:c}".format(ord(c) - 32)
        else:
            up += c
    print("{:s}".format(up))
