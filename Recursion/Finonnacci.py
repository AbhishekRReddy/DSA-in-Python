def fibonacci(n):
    if (n<2):
        return ModuleNotFoundError
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(25):
    print(fibonacci(i),end='---')

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55  ṇṇṇ