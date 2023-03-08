def my_bubble_sort(numbers):
    start = 0
    end = len(numbers) -1
    not_sorted = True
    while not_sorted:
        not_sorted = False
        for i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                not_sorted = True
        end -= 1

numbers = [4,8,1,2,10,47,55,1,0]
my_bubble_sort(numbers)
print(numbers)
