def is_sorted(numbers):
    for i, num in enumerate(numbers):
        if i == 0:
            prev = num
            continue
        if prev < num:
            continue
        else:
            return False
    return True
        
numbers = [n for n in range(1, 10)]
numbers[0] = 55
print(is_sorted(numbers))


