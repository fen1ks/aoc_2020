
def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)


def part_1(dep, buses):
    res = dict()
    for b in buses:
        v = b
        while v < dep:
            v += b
        res[v - dep] = b
    min_b = min(res.keys())
    print res[min_b] * min_b


def check(target, buses):
    res = [b2 - b1 for b1, b2 in zip(buses, buses[1:])]
    return res == target


def do_step(buses, steps, limit):
    last = buses[0]
    for idx, (b, s) in enumerate(zip(buses[1:limit], steps[1:limit])):

        n = (last - b) / s
        b += s * n
        if last >= b:
            b += s
        last = b
        buses[idx+1] = b


if __name__ == '__main__':
    with open('inputs/13.txt', 'r') as file:
        data = file.readlines()
    dep = int(data[0].strip())
    buses = [(idx, int(v)) for idx, v in enumerate(data[1].strip().split(',')) if v != 'x']
    target = [idx2 - idx for (idx, _), (idx2, _) in zip(buses, buses[1:])]
    buses = [v for _i, v in buses]
    steps = buses[::]
    # Part 1
    part_1(dep, buses)
    # Part 2

    steps_2 = [lcm(buses[0], buses[1])]
    for b in buses[2:-1]:
        steps_2.append(lcm(steps_2[-1], b))

    while not check(target[:1], buses[:2]):
        buses[0] += steps[0]
        do_step(buses, steps, 2)

    for idx in range(2, len(buses)):
        while not check(target[:idx], buses[:idx + 1]):
            buses[0] += steps_2[idx-2]
            do_step(buses, steps, idx + 1)
    print buses[0]



