def max_2(*args):
    max_value = max(args)
    args = list(args)
    args.remove(max_value)
    second = max(args)
    return second 