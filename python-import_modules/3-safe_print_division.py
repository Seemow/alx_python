def safe_print_division(a, b):
    try:
        division = a / b
    except Exception:
        division = None
    finally:
        print("Inside result: {}".format(division))
        return division


a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))