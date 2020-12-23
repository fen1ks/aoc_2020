
MAX = 9


def move(cups):
    curr = cups[0]
    picked = cups[1:4]
    dest = int(curr) - 1
    cups = [curr] + cups[4:]

    dest = MAX if dest == 0 else dest
    while dest in picked:
        dest -= 1
        dest = MAX if dest == 0 else dest
    #print 'curr:', curr, 'picked:', picked, 'dest:', dest, 'idx(curr)', cups.index(curr), 'idx(dest)', cups.index(dest)
    dest_idx = cups.index(dest)
    for idx, val in enumerate(picked, 1):
        cups.insert(dest_idx + idx, val)
    cups = cups[1:] + [cups[0]]
    return cups


if __name__ == '__main__':
    with open('inputs/23.txt', 'r') as file:
        data = file.read()
    cups = [int(v) for v in data] + range(len(data) + 1, MAX + 1)
    for _ in xrange(100):
        cups = move(cups)
    # print solution
    idx = cups.index(1)
    print ''.join(map(str, cups[idx+1:] + cups[:idx]))
