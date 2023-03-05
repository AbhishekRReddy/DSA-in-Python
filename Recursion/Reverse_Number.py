def reverse(num,rev_num = 0):
    if num <= 0:
        return rev_num
    rem = num % 10
    num = num // 10
    rev_num = rev_num * 10 + rem
    return reverse(num, rev_num)

print(reverse(789))
        