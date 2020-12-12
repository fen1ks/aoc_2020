from copy import deepcopy

adjacent = [(x, y) for x in (-1, 0 ,1) for y in (-1, 0, 1) if (x, y) != (0, 0)]

if __name__ == '__main__':
    with open('inputs/11.txt', 'r') as file:
        data = [[v for v in line.strip()] for line in file.readlines()]
    data = [['.'] + row + ['.'] for row in data]
    # left, rigt, top and bottom most with empty floor to avoid checking edge cases
    nx = len(data[0])
    ny = len(data) + 2
    data.insert(0, ['.']*nx)
    data.append(['.']*nx)

    round_idx = 0
    while True:
        curr_data = deepcopy(data)
        for rid, row in enumerate(curr_data[1:-1]):
            for cid, seat in enumerate(row[1:-1]):
                '''
                # part 1
                adjacent_seats = [curr_data[rid + x + 1][cid + 1 + y] for x, y in adjacent]
                occupied = sum(s == '#' for s in adjacent_seats)
                '''
                occupied = 0
                for x, y in adjacent:
                    curr_x = cid + x
                    curr_y = rid + y
                    while 0 <= curr_x < nx - 2 and 0 <= curr_y < ny - 2 and curr_data[curr_y + 1][curr_x + 1] == '.':
                        curr_x += x
                        curr_y += y
                    if curr_data[curr_y + 1][curr_x + 1] == '#':
                        occupied += 1
                if seat == 'L' and occupied == 0:
                    data[rid + 1][cid + 1] = '#'
                elif seat == '#' and occupied >= 5:
                    data[rid + 1][cid + 1] = 'L'
        if curr_data == data:
            print sum(seat == '#' for row in data for seat in row)
            break
        round_idx += 1
        #print 'ROUND', round_idx
        #print '\n'.join(''.join(row) for row in data)