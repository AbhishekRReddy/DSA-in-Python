def traingle(num):
    if num == 0:
        return 
    print('*' * num)
    traingle(num-1)

def iter_triangle(num):
    while num > 0:
        for _ in range(num):
            print('*', end='')
        print()
        num -= 1

def triangle(row, col = 1):
    if row == 0:
        return
    if row < col:
        print()
        triangle(row -1, 1)
    else:
        print('*', end= '')
        triangle(row, col+1)

triangle(5)


