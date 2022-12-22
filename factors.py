#!/usr/bin/python3


"""Importing module for getting the argv and exit"""


import sys
ac = len(sys.argv)
if(ac != 2):
    sys.exit(f"Usage: {sys.argv[0]} <file>")


"""Finding natural factors of a number"""


def factorizer(n):
    p = 2
    q = 2
    while (p * q <= n):
        while(p * q <= n):
            if (q * p == n):
                print("{} = {} * {}".format(n, q, p))
                return
            q += 1
        q = 2
        p += 1


"""Opening a test file containing test cases(n)"""


def file_open(file):
    with open(file) as f:
        for num in f:
            num = int(num)
            factorizer(num)


file_open(sys.argv[1])
