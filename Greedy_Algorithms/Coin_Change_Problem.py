'''
COIN CHANGE PROBLEM -- GREEDY APPROACH
Here, total amount and denominations will be given. We need to choose the minimum 
number of denomination to make the total amount.
1. Sort the denomination in non-increasing order. 
2. Choose the maximum value which is less than the current amount
3. Subtract the denominations from the total amount.
4. Repeat till you will reach Zero. 
'''
def coin_change(total_amount, denominations):
    denominations.sort(reverse = True)
    current_index = 0
    while True:
        if total_amount >= denominations[current_index]:
            print(denominations[current_index])
            total_amount -= denominations[current_index]
        if total_amount < denominations[current_index]:
            current_index += 1
        if total_amount == 0:
            return
        if current_index == len(denominations):
            print('Not possible')
            return

total_amount = 126
denomination = [2,5,10,50,100]
coin_change(total_amount, denomination)