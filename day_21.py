from collections import Counter, defaultdict
from itertools import combinations

if __name__ == '__main__':
    with open('inputs/21.txt', 'r') as file:
        data = [l.strip() for l in file.readlines()]

    foods = []

    c = Counter()
    total_a = set()
    total_i = set()
    for line in data:
        idx = line.find('(')
        ingredients = line[:idx - 1].split(' ')
        allergens = line[idx + 2 + len('contains'):-1].split(', ')
        foods.append((ingredients, allergens))
        total_a |= set(allergens)
        total_i |= set(ingredients)

    print 'allergens', len(total_a)
    print 'ingredients', len(total_i)
    print '-'*10
    known = dict()
    comb = []
    test = defaultdict(list)

    for (i1, a1), (i2, a2) in combinations(foods, 2):
        common_i = set(i1) & set(i2)
        common_a = set(a1) & set(a2)
        if len(a1) == 1:
            test[a1[0]].append(i1)
        if len(a2) == 1:
            test[a2[0]].append(i2)
        if len(common_a) == 1:
            c_a = list(common_a)[0]
            test[c_a].append(list(common_i))
        if len(common_a) == 1 and len(common_i) == 1:
            common_a = list(common_a)[0]
            common_i = list(common_i)[0]
            known[common_i] = common_a

    a_to_i = dict()
    while test:
        test2 = dict()
        for allergen, ingredients in test.items():
            common_i = set.intersection(*[set(i) for i in ingredients])
            a_to_i[allergen] = common_i
            if len(common_i) == 1:
                common_i = list(common_i)[0]
                known[common_i] = allergen
            else:
                test2[allergen] = [[c for c in l if c not in known] for l in ingredients]
        test = test2

    print known
    res = 0
    for ingredients, allergens in foods:
        res += sum(1 for i in ingredients if i not in known)
    print 'Part1:', res
    part2 = sorted(known.items(), key=lambda x: x[1])
    print 'Part2:', ','.join(v[0] for v in part2)
