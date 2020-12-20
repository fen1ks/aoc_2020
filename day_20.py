import re
from collections import Counter, defaultdict
from itertools import product
from operator import mul
from math import sqrt

tile_name = re.compile(r'Tile (\d+):')


def parse_tile(tile):
    t_idx = tile_name.match(tile[0]).group(1)
    top = tile[1]
    bottom = tile[-1]
    left = ''.join([r[0] for r in tile[1:]])
    right = ''.join([r[-1] for r in tile[1:]])
    return [{t_idx: (top, left, right, bottom)}, {t_idx: (top, left[::-1], right[::-1], bottom)}, {t_idx: (top[::-1], left, right, bottom[::-1])}]


def check(tiles_f):
    tiles_num = len(tiles_f)
    side_num = sqrt(tiles_num)
    single_edge_exp = side_num * 4
    common_edge_exp = (side_num - 1) * side_num * 2


    tiles = dict()
    for t in tiles_f:
        tiles.update(t)
    edge_to_tile = defaultdict(list)
    # build edge -> tile_idx
    for idx, t in tiles.items():
        for edge in t:
            edge_to_tile[edge].append(idx)

    # check common edges
    c = Counter()
    for t in tiles.values():
        c.update(t)
    l2 = len([e for e, count in c.items() if count == 2])
    l1 = len([e for e, count in c.items() if count == 1])
    if l2 != common_edge_exp or l1 != single_edge_exp:
        return

    common_edges_per_tile = defaultdict(int)
    # check number of common edges per tile
    for edge, count in c.items():
        if count != 2:
            continue
        for t_idx in edge_to_tile[edge]:
            common_edges_per_tile[t_idx] += 1
    #print len(common_edges_per_tile)
    tiles = [int(t) for t, cnt in common_edges_per_tile.items() if cnt == 2]
    return reduce(mul, tiles)

if __name__ == '__main__':
    with open('inputs/20.txt', 'r') as file:
        data = [l.strip() for l in file.readlines()]

    tiles_l = []
    idx = data.index('')
    while idx != -1:
        tiles_l.append(data[:idx])
        data = data[idx+1:]
        try:
            idx = data.index('')
        except:
            tiles_l.append(data)
            idx = -1

    tiles = []
    for t in tiles_l:
        tiles.append(parse_tile(t))

    print len(tiles)

    for tiles_f in product(*tiles):
        r = check(tiles_f)
        if r:
            print r
            break



