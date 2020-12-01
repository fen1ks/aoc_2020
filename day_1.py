from itertools import combinations


def solve_1(data, target):
    arr = sorted(int(v) for v in data.split())
    l_idx, r_idx = 0, len(arr) - 1
    while l_idx < r_idx:
        v_l, v_r = arr[l_idx], arr[r_idx]
        if v_l + v_r == target:
            print v_l * v_r
            break
        elif v_l + v_r > target:
            r_idx -= 1
        else:
            l_idx += 1
    else:
        raise ValueError('NO SOLUTION')


def solve_2(data, target, n_of_vals=3):
    arr = sorted(int(v) for v in data.split())
    for cand in combinations(arr, n_of_vals):
        if sum(cand) == target:
            print reduce(lambda a, b: a*b, cand)
            break
    else:
        raise ValueError('NO SOLUTION')


if __name__ == '__main__':
    with open('inputs/1.txt', 'r') as file:
        data = file.read()
    solve_1(data, 2020)
    solve_2(data, 2020)
