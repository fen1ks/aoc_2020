from collections import deque


def rec_combat(p1, p2, game_idx=1):
    cache = set()
    round_idx = 0
    while p1 and p2:
        round_idx += 1
        game_state = (tuple(p1), tuple(p2))
        if game_state in cache:
            #print 'state observed p1 wins'
            return 1
        else:
            cache.add(game_state)

        #print '-- Round {} (Game {}) --'.format(round_idx, game_idx)
        #print 'P1', p1
        #print 'P2', p2
        c1 = p1.popleft()
        c2 = p2.popleft()
        #print 'P1c', c1
        #print 'P2c', c2

        if c1 <= len(p1) and c2 <= len(p2):
            p_won = rec_combat(deque(list(p1)[:c1]), deque(list(p2)[:c2]), game_idx + 1)
            if p_won == 1:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        else:
            if c1 > c2:
                #print 'P1 wins'
                p1.append(c1)
                p1.append(c2)
            else:
                #print 'P2 wins'
                p2.append(c2)
                p2.append(c1)
    print 'Game {} ended. P{} wins'.format(game_idx, 1 if p1 else 2)
    print 'Part 2:', sum((idx + 1) * v for idx, v in enumerate(reversed(p1 or p2)))
    return 1 if p1 else 2

if __name__ == '__main__':
    with open('inputs/22.txt', 'r') as file:
        data = [l.strip() for l in file.readlines()]

    idx = data.index('')
    p1 = deque(int(v) for v in data[1:idx])
    p2 = deque(int(v) for v in data[idx+2:])

    # Part 1
    while p1 and p2:
        c1 = p1.popleft()
        c2 = p2.popleft()
        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    print 'Part 1:', sum((idx + 1) * v for idx, v in enumerate(reversed(p1 or p2)))

    # Part 2
    rec_combat(p1, p2)
