import re

cache = dict()
rules = dict()


def eval(rule_idx):
    if rule_idx in cache:
        return cache[rule_idx]
    rule = rules[rule_idx]
    # check if composite
    if '|' in rule:
        c_rule = [r.strip(' ') for r in rule.split('|')]
        e_rule = []
        for rule_ in c_rule:
            r = [int(v) for v in rule_.split(' ')]
            s_rule = ''.join([eval(rule) for rule in r])
            s_rule = '(?:' + s_rule + ')'
            e_rule.append(s_rule)
        f_rule = '|'.join(e_rule)
        f_rule = '(?:' + f_rule + ')'
        cache[rule_idx] = f_rule
        return f_rule
    # check if final rule
    elif '"' in rule:
        r = '(?:' + rule[1] + ')'
        cache[rule_idx] = r
        return r
    # concatenate ors
    else:
        r = [int(v) for v in rule.split(' ')]
        r = ''.join([eval(rule) for rule in r])
        cache[rule_idx] = r
        return r


if __name__ == '__main__':
    with open('inputs/19.txt', 'r') as file:
        data = [l.strip() for l in file.readlines()]

    messages = []

    idx = data.index('')
    messages = data[idx+1:]

    for rule in data[:idx]:
        idx = rule.find(':')
        rule_idx = int(rule[:idx])
        rule = rule[idx + 1:].strip(' ')
        rules[rule_idx] = rule

    # Part 1
    final_rule = eval(0)
    final_rule = re.compile('^' + final_rule + '$')
    result = 0
    for m in messages:
        if final_rule.match(m):
            result += 1
    print result
    # Part 2, manually create rule 0 from rules 42 and 31
    r42 = cache[42]
    r31 = cache[31]
    result = 0
    for idx in xrange(1, 40):
        idx = str(idx)
        final_rule_part_2 = r42 + '+' + r42 + '{' + idx + '}' + r31 + '{' + idx + '}'
        final_rule_part_2 = re.compile('^' + final_rule_part_2 + '$')
        for m in messages:
            if final_rule_part_2.match(m):
                result += 1
    print result






