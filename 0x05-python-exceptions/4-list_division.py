#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_lenght):
        try:
            new_list.append(my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except TypeError:
            new_list.append(0)
            print("wrong type")
        except IndexError:
            new_list.append(0)
            print("out of range")
        finally:
            pass
    return new_list
