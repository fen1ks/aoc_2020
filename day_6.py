from collections import Counter


if __name__ == '__main__':
    with open('inputs/6.txt', 'r') as file:
        data = [x.strip() for x in file.readlines()]
    data = [''] + data
    idx = [idx for idx, line in enumerate(data) if line == ''] + [len(data)]

    any_ = 0
    all_ = 0

    groups = list()
    for idx1, idx2 in zip(idx, idx[1:]):
         groups.append(data[idx1+1:idx2])
    for group in groups:
        c = Counter()
        for person in group:
            c.update(person)
        any_ += len(c.keys())
        all_ += len([k for k, v in c.items() if v == len(group)])

    print any_, all_


