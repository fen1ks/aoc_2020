import re


inst_r = re.compile(r'(\w{3}) ([+-])(\d*)')


def check(instructions):
    acc = 0
    seen = set()
    inst_id = 0
    while inst_id in instructions:
        if inst_id in seen:
            return False, acc
        seen.add(inst_id)
        i, s, v = instructions[inst_id]
        if i == 'acc':
            acc += eval(s + v)
            inst_id += 1
        elif i == 'jmp':
            inst_id += eval(s + v)
        else:
            inst_id += 1
    return True, acc

if __name__ == '__main__':
    with open('inputs/8.txt', 'r') as file:
        data = file.readlines()

    instructions = {idx: inst_r.match(line).groups() for idx, line in enumerate(data)}
    # part 1
    print check(instructions)[1]
    # part 2
    nj_instructions = [idx for idx, val in instructions.items() if val[0] in ('nop', 'jmp')]
    for idx in nj_instructions[2:]:
        inst = instructions.copy()
        i = inst[idx]
        i = ('jmp' if i[0] == 'nop' else 'nop', i[1], i[2])
        inst[idx] = i
        success, val = check(inst)
        if success:
            print val
            break
