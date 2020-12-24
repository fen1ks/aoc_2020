
MAX = 1000000


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


class LinkedList:

    def __init__(self):
        self.head = None
        self.nodes = None

    def __str__(self):
        return 'head: ' + str(self.head)

    def display(self):
        res = [str(self.head.val)]
        node = self.head.next
        while node != self.head:
            res.append(str(node.val))
            node = node.next
        print ','.join(res)


def move(cups):
    curr = cups[0]
    picked = cups[1:4]
    dest = int(curr) - 1
    cups = [curr] + cups[4:]

    dest = MAX if dest == 0 else dest
    while dest in picked:
        dest -= 1
        dest = MAX if dest == 0 else dest
    #print 'curr:', curr, 'picked:', picked, 'dest:', dest, 'idx(curr)', cups.index(curr), 'idx(dest)', cups.index(dest)
    dest_idx = cups.index(dest)
    cups = cups[:dest_idx + 1] + picked + cups[dest_idx + 1:]
    cups = cups[1:] + [cups[0]]
    return cups


def move_part_2(llist):
    curr = llist.head
    picked = [curr.next, curr.next.next, curr.next.next.next]
    dest = curr.val - 1

    dest = MAX if dest == 0 else dest
    picked_vals = [n.val for n in picked]
    while dest in picked_vals:
        dest -= 1
        dest = MAX if dest == 0 else dest

    # curr -> rest -> dest -> picked -> rest
    curr.next = picked[-1].next
    dest_node = llist.nodes[dest]
    picked[-1].next = dest_node.next
    dest_node.next = picked[0]

    # move curr to tail
    llist.head = curr.next


def part_1(data):
    cups = [int(v) for v in data] + range(len(data) + 1, MAX + 1)
    for _ in xrange(100):
        cups = move(cups)
    # print solution
    idx = cups.index(1)
    return ''.join(map(str, cups[idx + 1:] + cups[:idx]))


if __name__ == '__main__':
    with open('inputs/23.txt', 'r') as file:
        data = file.read()
    # Part 1
    #print part_1(data)

    # Part 2
    llist = LinkedList()
    cups = [int(v) for v in data] + range(len(data) + 1, MAX + 1)
    nodes = [Node(val) for val in xrange(MAX + 1)]
    llist.nodes = nodes
    for v1, v2 in zip(cups, cups[1:]):
        nodes[v1].next = nodes[v2]
    nodes[cups[-1]].next = nodes[cups[0]]
    llist.head = nodes[cups[0]]
    for _ in xrange(10000000):
        move_part_2(llist)
    print llist.nodes[1].next.val * llist.nodes[1].next.next.val


