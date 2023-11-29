#!/usr/bin/python3
for num in range(0, 99):
    if (num < 10):
        print(f"{num} = 0x{num}")
    elif (num >= 10):
        print(f"{num} = {hex(num)}")
