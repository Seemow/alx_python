def safe_print_division(a, b):
    try:
        division = a / b
    except Exception:
        division = None
    finally:
        print("Inside result: {}".format(division))
        return division

result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
