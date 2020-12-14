import re

r = re.compile(r'^mem\[(\d+)\] = (\d+)')


def create_comb(mask):
    x = len([v for v in mask if v == 'X'])
    masks = []
    for v in xrange(0, 2**x):
        sv = str(bin(v))[2:].zfill(x)
        new_mask = ''
        idx = 0
        for m in mask:
            if m == 'X':
                new_mask += sv[idx]
                idx += 1
            else:
                new_mask += m
        masks.append(new_mask)
    return masks

if __name__ == '__main__':
    with open('inputs/14.txt', 'r') as file:
        data = [line.strip() for line in file.readlines()]
    memory = dict()
    for line in data:
        if 'mask' in line:
            mask = line[7:]
            continue
        v, mem_val = r.match(line).groups()
        v = int(v)
        mem_val = int(mem_val)
        val = str(bin(v))[2:].zfill(36)
        nval = ''
        for vv, vm in zip(val, mask):
            if vm == '0':
                nval += vv
            elif vm == '1':
                nval += '1'
            else:
                nval += 'X'

        for v in create_comb(nval):
            mem_addr = int(v, 2)
            memory[mem_addr] = mem_val
    print sum(memory.values())
