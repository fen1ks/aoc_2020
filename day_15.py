from collections import defaultdict

if __name__ == '__main__':
    with open('inputs/15.txt', 'r') as file:
        data = [int(v) for v in file.readline().strip().split(',')]
    m = defaultdict(list)
    for idx, v in enumerate(data):
        m[v].append(idx + 1)
    last = data[-1]
    add = True
    round = len(data) + 1
    while round <= 30000000:
        if add:
            m[0].append(round)
            last = 0
            add = False
        else:
            spoken = m[last]
            last = spoken[-1] - spoken[-2]
            if last not in m:
                add = True
            m[last].append(round)
        round += 1
    print last