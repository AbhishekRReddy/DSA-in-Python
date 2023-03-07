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

iter_triangle(5)


