import re

pass_fields = re.compile(r'(\w+):([^ ]+)')


def validate_height(v):
    if re.match(r'\d+cm', v):
        return 150 <= int(v[:-2]) <= 193
    elif re.match(r'\d+in', v):
        return 59 <= int(v[:-2]) <= 76

pass_rules = {
    'byr': lambda v: len(v) == 4 and 1920 <= int(v) <= 2002,
    'iyr': lambda v: len(v) == 4 and 2010 <= int(v) <= 2020,
    'eyr': lambda v: len(v) == 4 and 2020 <= int(v) <= 2030,
    'hgt': validate_height,
    'hcl': lambda v: bool(re.match(r'#[0-9a-f]{6}$', v)),
    'ecl': lambda v: v in 'amb blu brn gry grn hzl oth'.split(' '),
    'pid': lambda v: bool(re.match(r'^\d{9}$', v)),
    'cid': lambda v: True,
}


def solve(validate_values=False):
    with open('inputs/4.txt', 'r') as file:
        data = file.readlines()
    # remove newlines
    data = (line.strip() for line in data)
    # replace empty string with chr(31) delimeter
    data = (line if line else chr(31) for line in data)
    # join line and split by chr(31)
    data = ' '.join(data)
    data = [line.strip(' ') for line in data.split(chr(31))]
    valid_count = 0
    for pass_data in data:
        fields = dict(pass_fields.findall(pass_data))
        valid = all(k in fields for k in pass_rules.keys() if k != 'cid')
        if validate_values:
            valid &= all(pass_rules[key](val) for key, val in fields.items())
        if valid:
            valid_count += 1
    return valid_count


if __name__ == '__main__':
    print solve(True)