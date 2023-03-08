import traceback
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
        traceback.print_stack()
        triangle(row -1, 1)
        print()
    else:        
        triangle(row, col+1)
        print('*', end= '')


triangle(5)



