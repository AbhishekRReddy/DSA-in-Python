def count_zero(num, count = 0):
    if num <= 0:
        return count
    rem = num % 10
    if rem == 0:
        count += 1
    return count_zero(num//10, count)

print(count_zero(1080595))





