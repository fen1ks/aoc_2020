import re


def get_next(expression):
    if not expression:
        return expression, expression
    if expression[0] in ('+', '*'):
        return expression[0], expression[1:]
    elif expression[0].isdigit():
        res = re.split(r'([+*)]*)', expression)
        return res[0], ''.join(res[1:])
    elif expression[0] == '(':
        pcount = 0
        for idx, c in enumerate(expression):
            if c == '(':
                pcount += 1
            elif c == ')':
                pcount -= 1
            if pcount == 0:
                return expression[1:idx], expression[idx + 1:]


def get_prev(expression):
    if not expression:
        return expression, expression
    if expression[-1] in ('+', '*'):
        return expression[-1], expression[:-1]
    elif expression[-1].isdigit():
        res = re.split(r'([+*(]*)', expression)
        return res[-1], ''.join(res[:-1])
    elif expression[-1] == ')':
        pcount = 0
        for idx, c in enumerate(reversed(expression)):
            if c == ')':
                pcount += 1
            elif c == '(':
                pcount -= 1
            if pcount == 0:
                return expression[-idx:-1], expression[:-idx-1]


def eval_1(expression):
    #print 'calling eval on', expression
    if expression.isdigit():
        return int(expression)
    left, rest = get_next(expression)
    op, rest = get_next(rest)
    right, rest = get_next(rest)
    #print 'left=', left, 'op=', op, 'right=', rest
    if op == '+':
        #print 'adding', left, right
        return eval_1(str(eval_1(left) + eval_1(right)) + rest)
    else:
        #print 'mult', left, right
        return eval_1(str(eval_1(left) * eval_1(right)) + rest)


def eval_2(expression):
    #print 'calling eval on', expression
    if expression.isdigit():
        return int(expression)
    if expression.lstrip('(').isdigit():
        return int(expression.lstrip('('))
    if expression.rstrip(')').isdigit():
        return int(expression.rstrip(')'))
    sum_idx = expression.find('+')
    if sum_idx != -1:
        left = expression[:sum_idx]
        right = expression[sum_idx + 1:]
        left, lrest = get_prev(left)
        right, rrest = get_next(right)
        return eval_2(lrest + str(eval_2(left) + eval_2(right)) + rrest)
    else:
        left, rest = get_next(expression)
        op, rest = get_next(rest)
        right, rest = get_next(rest)
        #print 'left=', left, 'op=', op, 'right=', rest
        if op == '+':
            #print 'adding', left, right
            return eval(str(eval(left) + eval(right)) + rest)
        else:
            #print 'mult', left, right
            return eval(str(eval(left) * eval(right)) + rest)


if __name__ == '__main__':
    with open('inputs/18.txt', 'r') as file:
        data = [line.strip() for line in file.readlines()]

    #part 1
    print sum(eval_1(line.replace(' ', '')) for line in data)

    # part 2
    print sum(eval_2(line.replace(' ', '')) for line in data)

