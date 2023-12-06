#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        av1 = int(argv[1])
        av2 = int(argv[3])
        operatr = argv[2]
        if operatr == "+":
            print("{:d} {} {:d} = {}".format(av1, operatr, av2, add(av1, av2)))
        elif operatr == "-":
            print("{:d} {} {:d} = {}".format(av1, operatr, av2, sub(av1, av2)))
        elif operatr == "*":
            print("{:d} {} {:d} = {}".format(av1, operatr, av2, mul(av1, av2)))
        elif operatr == "/":
            print("{:d} {} {:d} = {}".format(av1, operatr, av2, div(av1, av2)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
