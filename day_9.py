from collections import deque


PREAMBLE = 25


def is_valid(v, arr):
    arr = sorted(arr)
    l_idx, r_idx = 0, len(arr) - 1
    while l_idx < r_idx:
        v_l, v_r = arr[l_idx], arr[r_idx]
        if v_l + v_r == v:
            return True
        elif v_l + v_r > v:
            r_idx -= 1
        else:
            l_idx += 1
    return False

if __name__ == '__main__':
    with open('inputs/9.txt', 'r') as file:
        data = [int(v.strip()) for v in file.readlines()]
    target_part_2 = 0
    # part 1
    preamble = deque(data[:PREAMBLE])
    for v in data[PREAMBLE:]:
        if not is_valid(v, preamble):
            print v
            target_part_2 = v
            break
        preamble.popleft()
        preamble.append(v)
    # part 2
    idxl, idxr = 0, 0
    s = data[idxr]
    while idxl <= idxr < len(data):
        if s == target_part_2:
            res_arr = data[idxl:idxr+1]
            print min(res_arr) + max(res_arr)
            break
        if s < target_part_2:
            idxr += 1
            s += data[idxr]
        if s > target_part_2:
            s -= data[idxl]
            idxl += 1
    else:
        print 'no such pair'
