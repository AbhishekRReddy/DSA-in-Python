def fibo(n):
    if n == 0:
        print(0)
        return
    if n == 1:
        print(0)
        print(1)
        return 
    fibo_val1 = 0
    fibo_val2 = 1
    print(fibo_val1,end=' ')
    print(fibo_val2,end =' ')
    for i in range(2,n+1):
        temp = fibo_val1
        fibo_val1 = fibo_val2
        fibo_val2 = temp + fibo_val1
        print(fibo_val2,end= ' ')

fibo(150)

