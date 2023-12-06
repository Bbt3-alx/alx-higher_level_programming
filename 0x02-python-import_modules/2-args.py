#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    nb_args = len(argv) - 1
    if nb_args == 0:
        print("{:d} arguments.".format(nb_args))
    elif nb_args == 1:
        print("{:d} argument:".format(nb_args))
        print("{:d}: {:s}".format(nb_args, argv[nb_args]))
    else:
        print("{:d} arguments:".format(nb_args))
        for i in range(1, nb_args + 1):
            print("{:d}: {:s}".format(i, argv[i]))
