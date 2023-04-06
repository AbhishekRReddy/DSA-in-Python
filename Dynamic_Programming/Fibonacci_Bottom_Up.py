def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    x = 0
    y = 1
    for _ in range(1,n-1):
        curr_num = x + y
        x = y
        y = curr_num
    return curr_num

print(fibo(8))
