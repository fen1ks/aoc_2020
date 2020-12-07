import re
from collections import defaultdict

rule = re.compile(r'(\w+ \w+) bags?')
rule_c = re.compile(r'(\d* ?\w+ \w+) bags?')
row_rule = re.compile(r'(\d*) (\w+) (\w+)')


target = 'shiny gold'


def search(bag, rules):
    res = set()
    if bag not in rules:
        return set()
    for b in rules[bag]:
        res.add(b)
        res |= search(b, rules)
    return res


def search_2(bag, rules):
    res = 0
    if bag not in rules:
        return res
    for b, cnt in rules[bag]:
        res += cnt
        res += cnt * search_2(b, rules)
    return res

if __name__ == '__main__':
    with open('inputs/7.txt', 'r') as file:
        data = file.readlines()

    result_rules = defaultdict(set)

    # PART 1
    for line in data:
        rules_row = rule.findall(line)
        outer, inner = rules_row[0], rules_row[1:]
        for bag in inner:
            result_rules[bag].add(outer)

    res = set(result_rules[target])
    for bag in result_rules[target]:
        res |= search(bag, result_rules)
    print len(res)

    result_rules = defaultdict(list)

    # PART 2
    for line in data:
        rules_row = rule_c.findall(line)
        outer, inner = rules_row[0], rules_row[1:]
        for bag in inner:
            if bag.endswith('no other'):
                continue
            ir = row_rule.match(bag).groups()
            cnt = int(ir[0])
            b = ' '.join(ir[1:])
            result_rules[outer].append((b, cnt))

    res = 0
    for bag, cnt in result_rules[target]:
        res += cnt
        res += cnt * search_2(bag, result_rules)
    print res

