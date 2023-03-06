def is_sorted(numbers, index = 0):
    if index+1 >= len(numbers):
        return True
    
    if numbers[index] < numbers[index + 1]:
        return is_sorted(numbers, index+1)
    else:
        return False

numbers = [n for n in range(11)]
numbers[1] = 100
print(is_sorted(numbers))