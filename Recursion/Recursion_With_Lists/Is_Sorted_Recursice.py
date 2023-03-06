def is_sorted(numbers, index = 0):
    if index == len(numbers)-1 :
        return True
    return (numbers[index] < numbers[index+1]) and is_sorted(numbers, index+1)

numbers = [n for n in range(11)]
#numbers[1] = 100
print(is_sorted(numbers))