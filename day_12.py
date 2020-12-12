

map_ = {
    'E': 'ESWN'*4,
    'S': 'SWNE'*4,
    'W': 'WNES'*4,
    'N': 'NESW'*4,
}

map_dir_ = {
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0),
    'N': (0, -1),
}


def rotate_part_1(curr, command):
    d, a = command[0], int(command[1:])
    return map_[curr][a/90 if d == 'R' else -a/90]


def rotate_part_2(pos_w, command):
    d, a = command[0], int(command[1:])
    x, y = pos_w
    if a == 180:
        return -x, -y
    if (d == 'L' and a == 90) or (d == 'R' and a == 270):
        return y, -x
    if (d == 'R' and a == 90) or (d == 'L' and a == 270):
        return -y, x
    return (x, y)



def move(curr, command):
    d, dist = command[0], int(command[1:])
    x, y = curr
    xm, ym = map_dir_[d]
    x += xm*dist
    y += ym*dist
    return (x, y)


def move_f_part_1(curr, pos, command):
    d, dist = command[0], int(command[1:])
    x, y = pos
    xm, ym = map_dir_[curr]
    x += xm*dist
    y += ym*dist
    return (x, y)


def move_f_part_2(curr, pos_w, command):
    d, dist = command[0], int(command[1:])
    x, y = curr
    xm, ym = pos_w
    x += xm*dist
    y += ym*dist
    return (x, y)


if __name__ == '__main__':
    with open('inputs/12.txt', 'r') as file:
        data = [line.strip() for line in file.readlines()]

    curr = 'E'
    pos_s = [0, 0]
    pos_w = [10, -1]

    for command in data:
        d, a = command[0], int(command[1:])
        #print 'pos', pos_w, pos_s
        #print 'command', command
        if d in ('L', 'R'):
            pos_w = rotate_part_2(pos_w, command)
        elif d == 'F':
            pos_s = move_f_part_2(pos_s, pos_w, command)
        else:
            pos_w = move(pos_w, command)
    print abs(pos_s[0]) + abs(pos_s[1])