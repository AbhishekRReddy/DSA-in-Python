def reverse(num, sum = 0):
    if num <= 0:
        return sum
    rem = num % 10
    sum = sum * 10 + rem
    return reverse(num//10, sum)

print(reverse(456))
        