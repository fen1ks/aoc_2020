import re
from collections import Counter


m = re.compile(r'(\d+)-(\d+) (\w): (\w+)')


def check_password(line):
    if not m.match(line):
        raise ValueError('Invalid line {}'.format(line))
    l, u, char, password = m.match(line).groups()
    c = Counter(password)
    l, u = int(l), int(u)
    return l <= c[char] <= u


def check_password_2(line):
    if not m.match(line):
        raise ValueError('Invalid line {}'.format(line))
    idx1, idx2, char, password = m.match(line).groups()
    idx1, idx2 = int(idx1), int(idx2)
    return (password[idx1 - 1] == char) ^ (password[idx2 - 1] == char)


if __name__ == '__main__':
    with open('inputs/2.txt', 'r') as file:
        data = file.readlines()
    print(sum([check_password(line) for line in data]))
    print(sum([check_password_2(line) for line in data]))


