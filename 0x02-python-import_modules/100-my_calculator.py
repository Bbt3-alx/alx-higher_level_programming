#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    num1 = int(args[1])
    operator = args[2]
    num2 = int(args[3])
    if operator == '+':
        print("{:d} + {:d} = {:d}".format(num1, num2, add(num1, num2)))
    elif operator == '-':
        print("{:d} - {:d} = {:d}".format(num1, num2, sub(num1, num2)))
    elif operator == '*':
        print("{} * {} = {}".format(num1, num2, mul(num1, num2)))
    elif operator == '/':
        print("{:d} / {:d} = {:d}".format(num1, num2, div(num1, num2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
