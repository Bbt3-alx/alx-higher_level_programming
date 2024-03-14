#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    nb_args = len(args) - 1

    if nb_args == 0:
        print("{:d} arguments.".format(nb_args))
    elif nb_args == 1:
        print("{:d} argument:".format(nb_args))
        print("{:d}: {:s}".format(nb_args, args[1]))
    else:
        print("{:d} arguments:".format(nb_args))
        for arg in range(1, nb_args + 1):
            print("{:d}: {:s}".format(arg, args[arg]))
