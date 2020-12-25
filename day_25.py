

def transform(number, loop_size):
    val = 1
    for _ in xrange(loop_size):
        val *= number
        val %= 20201227
    return val


def transform_2(number, loop_size):
    return exponentMod(number, loop_size, 20201227)


def exponentMod(A, B, C):
    # Base Cases
    if (A == 0):
        return 0
    if (B == 0):
        return 1

    # If B is Even
    y = 0
    if (B % 2 == 0):
        y = exponentMod(A, B / 2, C)
        y = (y * y) % C

        # If B is Odd
    else:
        y = A % C
        y = (y * exponentMod(A, B - 1,
                             C) % C) % C
    return ((y + C) % C)


def guess_loop(pub_key, max_loop=20000000):
    for loop_size in xrange(1, max_loop):
        if transform_2(7, loop_size) == pub_key:
            return loop_size
    raise ValueError('Cannot guess loop size')


if __name__ == '__main__':
    with open('inputs/25.txt', 'r') as file:
        pub1, pub2 = [int(v) for v in file.read().split('\n')]

    loop1 = guess_loop(pub1)
    loop2 = guess_loop(pub2)
    print 'Part1:', transform(pub2, loop1)