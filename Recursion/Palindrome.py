def reverse(num, sum = 0):
    if num <= 0:
        return sum
    rem = num % 10
    sum = sum * 10 + rem
    return reverse(num//10, sum)


def palindrome(num):
    rev_num = reverse(num)
    if num == rev_num:
        return True
    else:
        return False

print(palindrome(19191))
        