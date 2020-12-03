def solve(right, down):
    with open('inputs/3.txt', 'r') as file:
        data = file.read().split()

    n = len(data[0])
    c = [row[right*idx % n] == '#' for idx, row in enumerate(data[::down])]
    return sum(c)

if __name__ == '__main__':
    print solve(1, 1) * solve(3, 1) * solve(5, 1) * solve(7, 1) * solve(1, 2)