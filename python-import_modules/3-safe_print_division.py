def safe_print_division(a, b):
    try:
        division = a / b
    except Exception:
        division = None
    finally:
        print("Inside result: {}".format(division))
        print("{:d} / {:d} = {}".format(a, b, division))
        