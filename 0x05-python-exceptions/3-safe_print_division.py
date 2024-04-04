#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = int(a) / int(b)
        return result
    except (ZeroDivisionError, TypeError, ValueError):
        return None
    finally:
        print("Inside result:{}".format(result))
