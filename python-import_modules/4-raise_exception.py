def raise_exception():
    try:
        return 1 / 0
    except Exception:
        print("Exception raised")