#!/usr/bin/python3

from sys import argv

i = len(argv) - 1
if i < 1:
    print("{} arguments.".format(i))
elif i == 1:
    print("{} argument:".format(i))
else:
    print("{} arguments:".format(i))

for j in range(i):
    print("{}: {:s}".format(j + 1, argv[j + 1]))
