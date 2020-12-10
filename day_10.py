from collections import Counter
from itertools import groupby, combinations


def is_valid(data):
    return all(abs(a-b) <= 3 for a, b in zip(data, data[1:]))


def check_cand(cand, data):
    n = 1
    for r in xrange(1, len(cand) + 1):
        for c in combinations(cand, r):
            d = [v for i, v in enumerate(data) if i not in c]
            n += is_valid(d)
    return n

if __name__ == '__main__':
    with open('inputs/10.txt', 'r') as file:
        data = sorted([int(v) for v in file.readlines()])

    # PART 1
    res = [data[0]]
    for v1, v2 in zip(data, data[1:]):
        res.append(v2 - v1)
    res.append(3)
    c = Counter(res)
    print c[1] * c[3]

    # PART 2
    data.append(0)
    data.append(max(data) + 3)
    data = sorted(data)
    n = 1
    cnd = [idx+1 for idx, (b, v, a) in enumerate(zip(data, data[1:], data[2:])) if a - b <= 3]
    for _, group in groupby(enumerate(cnd), lambda (index, item): abs(index - item)):
        g = [v[1] for v in group]
        if len(g) == 1:
            n *= 2
        else:
            n *= check_cand(g, data)
    print n



