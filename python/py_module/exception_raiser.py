def raise_exception(throw:bool):
    if throw:
        raise RuntimeError("This is my exception")
    return True
