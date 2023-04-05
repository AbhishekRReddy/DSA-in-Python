def fibo(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if not n in memo:
        memo[n] = fibo(n-1,memo) + fibo(n-2,memo)
        #Only one time the value for the each will stored in disctionary
    return memo[n]

dict ={}
print(fibo(5,dict))
