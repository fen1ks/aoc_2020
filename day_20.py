import re
from collections import Counter, defaultdict
from operator import mul
from math import sqrt

tile_name = re.compile(r'Tile (\d+):')


def parse_tile_edges(tile):
    t_idx = tile_name.match(tile[0]).group(1)
    top = tile[1]
    bottom = tile[-1]
    left = ''.join([r[0] for r in tile[1:]])
    right = ''.join([r[-1] for r in tile[1:]])
    return {t_idx: (top, top[::-1], bottom, bottom[::-1], left, left[::-1], right, right[::-1])}


def parse_tile(tile):
    t_idx = tile_name.match(tile[0]).group(1)
    return {int(t_idx): tile[1:]}


def get_right(tile):
    return ''.join(row[-1] for row in tile)


def get_left(tile):
    return ''.join(row[0] for row in tile)


def get_bottom(tile):
    return tile[-1]


def get_top(tile):
    return tile[0]


def rotate(tile):
    rows = []
    for idx in xrange(len(tile) - 1, -1, -1):
        rows.append(''.join(row[idx] for row in tile))
    return rows


def flip(tile):
    return [row[::-1] for row in tile]


def get_next_rot(tile):
    yield tile
    tile = rotate(tile)
    yield tile
    tile = rotate(tile)
    yield tile
    tile = rotate(tile)
    yield tile
    tile = flip(tile)
    yield tile
    tile = rotate(tile)
    yield tile
    tile = rotate(tile)
    yield tile
    tile = rotate(tile)
    yield tile


def print_tile(tile):
    print '\n'.join(tile)


def is_monster(x, y, tile):
    row0 = tile[y]
    row1 = tile[y + 1]
    row2 = tile[y + 2]
    p1 = row0[x + 18] == '#'
    p2 = row1[x] == '#' and row1[x + 5:x + 7] == '##' and row1[x + 11:x + 13] == '##' and row1[x + 17:x + 20] == '###'
    p3 = row2[x + 1] == '#' and row2[x + 4] == '#' and row2[x + 7] == '#' and row2[x + 10] == '#' and row2[x + 13] == '#' and row2[x + 16] == '#'
    return p1 and p2 and p3


def find_monsters(tile):
    res = 0
    for row_idx in xrange(0, len(tile) - 3):
        for col_idx in xrange(0, len(tile[0]) - 20):
            res += is_monster(col_idx, row_idx, tile)
    return res


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

    #print len(tiles_l)

    tiles = dict()
    for t in tiles_l:
        tiles.update(parse_tile_edges(t))
    edge_to_tile = defaultdict(list)
    # build edge -> tile_idx
    for idx, t in tiles.items():
        for edge in t:
            edge_to_tile[edge].append(idx)

    # check common edges
    c = Counter()
    for t in tiles.values():
        c.update(t)

    common_edges_per_tile = defaultdict(int)
    # check number of common edges per tile
    for edge, count in c.items():
        if count != 2:
            continue
        for t_idx in edge_to_tile[edge]:
            common_edges_per_tile[t_idx] += 1
    # print len(common_edges_per_tile)
    min_val = sorted(common_edges_per_tile.values())[0]
    corner_tiles = [int(tile) for tile, count in common_edges_per_tile.items() if count == min_val]
    #print 'corner tiles', corner_tiles
    print 'Part1:', reduce(mul, corner_tiles)

    # PART 2
    tiles_whole = dict()
    for t in tiles_l:
        tiles_whole.update(parse_tile(t))

    tile_idx = corner_tiles[0]
    row_len = int(sqrt(len(tiles_l)))
    solution = []
    # first row
    row = []
    tile = tiles_whole[tile_idx]
    # rotate so common edges are right and bottom
    for t in get_next_rot(tile):
        r = get_right(t)
        b = get_bottom(t)
        re = edge_to_tile[r]
        be = edge_to_tile[b]
        if len(re) == 2 and len(be) == 2:
            break
    row.append((tile_idx, t))

    for _ in xrange(row_len - 1):
        next_tile_idx = list(set([int(v) for v in re]) - {tile_idx})[0]
        next_tile = tiles_whole[next_tile_idx]
        # rotate so right prev and left curr edges align
        for t in get_next_rot(next_tile):
            curr_l = get_left(t)
            if curr_l == r:
                break
        row.append((next_tile_idx, t))
        r = get_right(t)
        re = edge_to_tile[r]
        tile_idx = next_tile_idx
    # add first row to solution
    solution.append(row)

    prev_rev = row
    row = []

    for _ in xrange(row_len - 1):
        for tile_idx, top_tile in prev_rev:
            b = get_bottom(top_tile)
            be = edge_to_tile[b]
            next_tile_idx = list(set([int(v) for v in be]) - {tile_idx})[0]
            next_tile = tiles_whole[next_tile_idx]
            # rotate so right prev and left curr edges align
            for t in get_next_rot(next_tile):
                curr_t = get_top(t)
                if curr_t == b:
                    break
            row.append((next_tile_idx, t))
        solution.append(row)
        prev_rev = row
        row = []

    # solution indexes
    #for sol_row in solution:
    #    print [t[0] for t in sol_row]

    solution_tile = []
    for sol_row in solution:
        for row_idx in xrange(1, len(sol_row[0][1]) - 1):
            row = ''
            for col_idx in xrange(len(sol_row)):
                row += sol_row[col_idx][1][row_idx][1:-1]
            solution_tile.append(row)

    total_hash = sum([c == '#' for row in solution_tile for c in row])
    total_monsters = max(find_monsters(s_tile) for s_tile in get_next_rot(solution_tile))
    print 'Part1:', total_hash - total_monsters * 15








