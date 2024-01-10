#!/usr/bin/python3
from hidden_4 import *
alln = dir()
for i in range(0, len(alln)):
    if alln[i][:2] != "__":
        print("{:s}".format(alln[i]))
