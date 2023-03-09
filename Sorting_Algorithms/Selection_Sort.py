def selection_sort(numbers):
    num_len = len(numbers)
    for i in range(num_len):
        min_index = i
        for j in range(i+1, num_len):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]                



numbers = [4,1,2,6,7,3,7,11,13,0,1,2,3]
selection_sort(numbers)
print(numbers)  