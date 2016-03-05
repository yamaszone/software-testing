def find(a, b, c):
    if a > c and a > b:
        return a
    elif c > b:
        return c
    else:
        return b