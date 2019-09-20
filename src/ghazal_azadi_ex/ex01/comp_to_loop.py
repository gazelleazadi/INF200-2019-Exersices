def squares_by_loop(n):
    s = []
    for k in range(n):
        if k % 3 == 1:
            s.append(k**2)
    return s


def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]


if __name__ == '__main__':
    num = 5
    if squares_by_loop(num) != squares_by_comp(num):
        print('ERROR!')
