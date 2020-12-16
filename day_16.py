import re
from collections import defaultdict

ticket = re.compile(r'(\d+-\d+)')

if __name__ == '__main__':
    with open('inputs/16.txt', 'r') as file:
        data = [line.strip() for line in file.readlines()]
    # part 1
    valid_tickets = []
    rules = []
    rules_2 = defaultdict(list)
    idx = 0
    for line in data:
        if not line:
            break
        r = ticket.findall(line)
        field = line[:line.find(':')]
        for v in r:
            v1, v2 = [int(d) for d in v.split('-')]
            rules.append((v1, v2))
            rules_2[field].append((v1, v2))
        idx += 1
    wrong = 0
    my_ticket = [int(v) for v in data[idx+2].split(',')]
    for line in data[idx+5:]:
        valid = True
        for val in line.split(','):
            val = int(val)
            if not any(a <= val <= b for a, b in rules):
                wrong += val
                valid = False
        if valid:
            valid_tickets.append(line)
    print wrong
    # part 2
    fields = rules_2.keys()
    values = [[int(v) for v in line.split(',')] for line in valid_tickets]
    values_for_idx = [[val[idx] for val in values] for idx in range(len(values[0]))]
    matching = defaultdict(list)
    matched = dict()
    for field in fields:
        for idx, values in enumerate(values_for_idx):
            if all(any(a <= val <= b for a, b in rules_2[field]) for val in values):
                matching[field].append(idx)
    matching = list(matching.items())
    matching = sorted(matching, key=lambda v: len(v[1]))
    matched_s = set()
    for field, values in matching:
        v = list(set(values) - matched_s)[0]
        matched[field] = v
        matched_s.add(v)
    calc_fields_idx = [val for field, val in matched.items() if 'departure' in field]
    print reduce(lambda a, b : a*b, [my_ticket[idx] for idx in calc_fields_idx])






