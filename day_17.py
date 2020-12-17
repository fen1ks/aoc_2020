from copy import deepcopy

N_OF_ROUNDS = 6


neighbours = [(x, y, z, w) for x in xrange(-1, 2) for y in xrange(-1, 2)
              for z in xrange(-1, 2) for w in xrange(-1, 2) if (x, y, z, w) != (0, 0, 0, 0)]


def print_cube(cube, n):
    total = len(cube[0])
    offset = (total - n) // 2
    for w in xrange(offset, offset + n):
        for z in xrange(offset, offset + n):
            print 'z =', z-total//2, 'w =', w-total//2
            for row in cube[w][z][offset:offset + n]:
                print ''.join(row[offset:offset + n])


def get_val(cube, coord):
    n = len(cube[0])
    x, y, z, w = coord
    if w < 0 or w >= n:
        return '.'
    if z < 0 or z >= n:
        return '.'
    if y < 0 or y >= n:
        return '.'
    if x < 0 or x >= n:
        return '.'
    return cube[w][z][y][x]


def play_round(cube):
    c = deepcopy(cube)
    n = len(c[0])
    for w in xrange(n):
        for z in xrange(n):
            for y in xrange(n):
                for x in xrange(n):
                    ns = [get_val(c, (x + xn, y + yn, z + zn, w + wn)) for xn, yn, zn, wn in neighbours]
                    active = len([v for v in ns if v == '#'])
                    curr = c[w][z][y][x]
                    if curr == '#':
                        if active in (2, 3):
                            cube[w][z][y][x] = '#'
                        else:
                            cube[w][z][y][x] = '.'
                    else:
                        if active == 3:
                            cube[w][z][y][x] = '#'
                        else:
                            cube[w][z][y][x] = '.'


if __name__ == '__main__':
    with open('inputs/17.txt', 'r') as file:
        data = [l.strip() for l in file.readlines()]
    n = len(data[0])
    total = n + 2 * N_OF_ROUNDS
    cube = [[[['.'] * total for _ in xrange(total)] for _ in xrange(total)] for _ in xrange(total)]
    # set input data
    initial_slice = cube[N_OF_ROUNDS + 1][N_OF_ROUNDS + 1]
    for idx_y in xrange(n):
        for idx_x in xrange(n):
            initial_slice[N_OF_ROUNDS + idx_y][N_OF_ROUNDS + idx_x] = data[idx_y][idx_x]
    for _ in xrange(N_OF_ROUNDS):
        play_round(cube)
    #print_cube(cube, 5)
    active = 0
    for w in xrange(total):
        for z in xrange(total):
            for y in xrange(total):
                for x in xrange(total):
                    if cube[w][z][y][x] == '#':
                        active += 1
    print active
