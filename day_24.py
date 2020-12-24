import re

directions = re.compile('e|se|sw|w|nw|ne')

move_map = {
    'e': (1, 0),
    'se': (0.5, -1),
    'sw': (-0.5, -1),
    'w': (-1, 0),
    'ne': (0.5, 1),
    'nw': (-0.5, 1),
}

neighbours = move_map.values()

def parse_moves(moves):
    x, y = 0, 0
    for m in moves:
        dx, dy = move_map[m]
        x += dx
        y += dy
    return x, y


def apply_tile_rules(tiles):
    new_black_tiles = set()
    # tiles to consider = black tiles + it's neihbours (white tiles)
    black_tiles = tiles
    white_tiles = {(x + dx, y + dy) for x, y in list(tiles) for dx, dy in neighbours}
    for w_tile in white_tiles:
        x, y = w_tile
        tile_n = {(x + dx, y + dy) for dx, dy in neighbours}
        if len(tile_n & black_tiles) == 2:
            new_black_tiles.add((x, y))
    for b_tile in black_tiles:
        x, y = b_tile
        tile_n = {(x + dx, y + dy) for dx, dy in neighbours}
        black_tile_n = len(tile_n & black_tiles)
        if black_tile_n == 0 or black_tile_n > 2:
            continue
        else:
            new_black_tiles.add((x, y))
    return new_black_tiles



if __name__ == '__main__':
    with open('inputs/24.txt', 'r') as file:
        data = [l.strip() for l in file.readlines()]

    flipped_tiles = set()

    for line in data:
        tile_coord = parse_moves(directions.findall(line))
        if tile_coord not in flipped_tiles:
            flipped_tiles.add(tile_coord)
        else:
            flipped_tiles.remove(tile_coord)
    # Part 1
    print 'Part 1', len(flipped_tiles)
    for day_idx in xrange(1, 101):
        flipped_tiles = apply_tile_rules(flipped_tiles)
        #print 'Day', day_idx, len(flipped_tiles)
    print 'Part 2', len(flipped_tiles)

