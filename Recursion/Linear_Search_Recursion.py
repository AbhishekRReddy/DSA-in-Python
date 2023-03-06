def recursive_search(numbers, value, index = 0):
    if index == len(numbers):
        return 'Value is Not Found'
    if numbers[index] == value:
        return index
    return recursive_search(numbers, value, index+1)

numbers = [n for n in range(10,60,5)]
print(numbers)
print(recursive_search(numbers, 55))