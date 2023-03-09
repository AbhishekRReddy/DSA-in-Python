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

def bubble_sort(numbers):
    for i in range(len(numbers)-1):
        is_sorted = True
        for j in range(0, len(numbers)-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                is_sorted = False 
        if is_sorted:
            return



numbers = [4,8,1,2,10,-47,55,1,0]
bubble_sort(numbers)
print(numbers)
