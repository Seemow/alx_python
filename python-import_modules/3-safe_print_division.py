def safe_print_division(a, b):
    try:
        division = a / b
    except Exception:
        division = None
    else:
        print("Inside result: {}".format(division))
    finally:
        print("{:d} / {:d} = {}".format(a, b, division))
        