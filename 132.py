def argv_int(*args):
    sanoq = 0
    for i in args:
        if type(i) == int:
            sanoq += 1
    return sanoq