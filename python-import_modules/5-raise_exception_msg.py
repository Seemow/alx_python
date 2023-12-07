def raise_exception_msg(message=""):
    try:
        return message
    except NameError as ne:
        print(ne)