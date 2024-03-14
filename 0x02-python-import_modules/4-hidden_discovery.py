#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    dirall = dir()
    for i in range(1, len(dirall)):
        if dirall[i][:2] != '__':
            print(dirall[i])
