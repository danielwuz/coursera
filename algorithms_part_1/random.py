# generate randint(0, n) by rand1()
def rand1():
    from random import randint
    return randint(0, 1)


# TODO: key to this problem: binary representation
def randn(n):
    if n == 0:
        return 0
    if n < 0:
        return -randn(-n)
    # determine how many bits needed
    bits = 1
    while (1 << bits) < n:
        bits += 1

    # very important, see how to ensure uniform distribution
    while True:
        x = 0
        for i in range(bits):
            x = (x << 1) | rand1()
        if x <= n:
            return x
