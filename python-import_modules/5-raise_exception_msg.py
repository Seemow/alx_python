def raise_exception_msg(message=""):
    try:
        pass
    except NameError as ne:
        print(ne)
    finally:
        return message
    