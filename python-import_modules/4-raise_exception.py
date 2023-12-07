def raise_exception():
    try:
        raise TypeError
    except Exception:
        print("Exception has been raised")