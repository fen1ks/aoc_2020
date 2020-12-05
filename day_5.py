
def calc(data, upper_sign, upper_limit):
    f, b = 0, upper_limit
    for s in data:
        d = b - f + 1
        if s == upper_sign:
            b -= d/2
        else:
            f += d/2
    return f

if __name__ == '__main__':
    with open('inputs/5.txt', 'r') as file:
        data = [row.strip() for row in file.readlines()]
    seat_ids = [calc(row[:7], 'F', 127) * 8 + calc(row[-3:], 'L', 7) for row in data]
    max_seat_id = max(seat_ids)
    missing_seat_ids = set(range(890)) - set(seat_ids)
    for seat_id in missing_seat_ids:
        if not {seat_id-1, seat_id+1} & missing_seat_ids:
            print seat_id
