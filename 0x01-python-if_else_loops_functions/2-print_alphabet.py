#!/usr/bin/python3
for alpha in range(ord('a'), ord('z') + 1):
    if (chr(alpha) in "qe"):
        continue
    print(chr(alpha), end='')
